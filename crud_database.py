import pandas as pd
import glob
import os
from sqlalchemy import inspect, text
from database.connection import engine
from database.models.base import Model
from database.models.busy_models import * 
from logging_config import logger
from datetime import date
from datetime import timedelta


end_date = date.today().strftime("%d-%m-%Y")

Model.metadata.create_all(bind=engine)

def truncate_all_tables(tables=None):
    inspector = inspect(engine)
    all_table_names = inspector.get_table_names()
    
    if tables is None:
        tables_to_truncate = all_table_names
    else:
        tables_to_truncate = [table for table in tables if table in all_table_names]

    with engine.connect() as connection:
        connection.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

        for table_name in tables_to_truncate:
            connection.execute(text(f"TRUNCATE TABLE `{table_name}`"))

        connection.execute(text("SET FOREIGN_KEY_CHECKS = 1"))

    print(f"Tables truncated successfully: {', '.join(tables_to_truncate)}")

def get_report_type(path: str) -> str:
    try:
        return path.split(os.sep)[-1].split('_')[1]
    except IndexError:
        logger.error(f"Invalid file path format: {path}")
        raise ValueError(f"Invalid file path format: {path}")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
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

def get_table_name(report_type: str) -> str:
    table_name = {
        "purchase": "busy_rm_purchase",
        "purchase-order": "busy_rm_purchase_order",
        'mitp': 'busy_rm_mitp',
        'mrfp': 'busy_rm_mrfp'
    }
    return table_name.get(report_type, "Key not found")

def process_files(root_folder: str):
    full_pattern = os.path.join(root_folder, "**", f"*{end_date}.xlsx")
    
    for file_path in glob.glob(full_pattern, recursive=True):
        try:
            report_type = get_report_type(file_path)
            if report_type in ['purchase', 'purchase-order','mrfp','mitp']:
                logger.info(f"Processing file: {file_path}")
                df = pd.read_excel(file_path, skiprows=3,skipfooter=1)
                df = clean_data(df)
                
                if df.empty:
                    logger.warning(f"No data to insert from file {file_path}.")
                    continue
                
                table_name = get_table_name(report_type)
                
                if table_name != "Key not found":
                    df.to_sql(table_name, engine, index=False, if_exists='append', chunksize=500)
                    logger.info(f"Data from {file_path} successfully inserted into table {table_name}.")
                else:
                    logger.error(f"Table name not found for report type: {report_type}")
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {e}")

def delete_table_data(start_date:str , end_date:str,table_name:str):
    pass




process_files(r"D:\UserProfile\Desktop\data")


    
    
