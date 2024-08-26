import pandas as pd
import glob
import os
from sqlalchemy import inspect, text
from sqlalchemy.orm import sessionmaker
from database.connection import engine
from database.models.base import Model
from database.models.busy_models import * 
from logging_config import logger
from datetime import datetime,date

current_date = datetime.now().date()
start_date = date(current_date.year, 4, 1)

start_date = start_date.strftime('%d-%m-%Y')
today_date = current_date.strftime('%d-%m-%Y')

class DataProcessor:
    def __init__(self, root_folder: str):
        self.root_folder = root_folder
        self.engine = engine
        Model.metadata.create_all(bind=self.engine)
        # Create a configured "Session" class
        self.Session = sessionmaker(bind=self.engine)
    
    def truncate_all_tables(self, tables=None):
        inspector = inspect(self.engine)
        all_table_names = inspector.get_table_names()

        if tables is None:
            tables_to_truncate = all_table_names
        else:
            tables_to_truncate = [table for table in tables if table in all_table_names]

        with self.engine.connect() as connection:
            connection.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

            for table_name in tables_to_truncate:
                connection.execute(text(f"TRUNCATE TABLE `{table_name}`"))

            connection.execute(text("SET FOREIGN_KEY_CHECKS = 1"))

        print(f"Tables truncated successfully: {', '.join(tables_to_truncate)}")
    
    def get_report_type(self, path: str) -> str:
        try:
            return path.split(os.sep)[-1].split('_')[1]
        except IndexError:
            logger.error(f"Invalid file path format: {path}")
            raise ValueError(f"Invalid file path format: {path}")
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # Log original columns for debugging
        logger.debug(f"Original columns: {df.columns.tolist()}")
        
        # Clean column names
        df.columns = df.columns.str.replace('/', '_')
        df.columns = df.columns.str.replace('.', '')
        df.columns = df.columns.str.replace(' ', '_')
        df.columns = df.columns.str.lower().str.replace('type', 'types')
        
        # Log cleaned columns for debugging
        logger.debug(f"Cleaned columns: {df.columns.tolist()}")
        
        # Drop first column if it contains null values
        first_col = df.columns[0]
        if df[first_col].isnull().any():
            df = df.drop(columns=first_col)
        
        # Forward-fill missing values
        df = df.fillna(method='ffill')
        
        return df

    def get_table_name(self, report_type: str) -> str:
        table_name = {
            "purchase": "busy_purchase",
            "purchase-order": "busy_purchase_order"
        }
        return table_name.get(report_type, "Key not found")
    
    def process_files(self):
        full_pattern = os.path.join(self.root_folder, '**', '*.xlsx')
        
        for file_path in glob.glob(full_pattern, recursive=True):
            session = self.Session()  # Create a new session
            try:
                report_type = self.get_report_type(file_path)
                if report_type in ['purchase', 'purchase-order']:
                    logger.info(f"Processing file: {file_path}")
                    df = pd.read_excel(file_path, skiprows=3, skipfooter=1)
                    df = self.clean_data(df)
                    
                    if df.empty:
                        logger.warning(f"No data to insert from file {file_path}.")
                        continue
                    
                    table_name = self.get_table_name(report_type)
                    
                    if table_name != "Key not found":
                        # Count rows before insertion
                        before_count = session.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
                        logger.info(f"Rows before insertion in {table_name}: {before_count}")

                        # Insert data
                        df.to_sql(table_name, self.engine, index=False, if_exists='append', chunksize=500)
                        session.commit()  # Commit the transaction if successful

                        # Count rows after insertion
                        after_count = session.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
                        logger.info(f"Rows after insertion in {table_name}: {after_count}")

                        # Log how many rows were added
                        rows_added = after_count - before_count
                        logger.info(f"Rows added to {table_name}: {rows_added}")
                    else:
                        logger.error(f"Table name not found for report type: {report_type}")
            except Exception as e:
                session.rollback()  # Rollback the transaction in case of error
                logger.error(f"Error processing file {file_path}: {e}")
            finally:
                session.close()  # Close the session

if __name__ == "__main__":
    root_folder_path = rf"D:\UserProfile\Desktop\data\busy_export_data\{today_date}"
    processor = DataProcessor(root_folder_path)
    processor.truncate_all_tables()
