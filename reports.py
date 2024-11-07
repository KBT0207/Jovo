# import pandas as pd

# path_pur = r"D:\UserProfile\Desktop\purchase.xlsx"
# path_mrfp = r"D:\UserProfile\Desktop\mrfp.xlsx"
# def clean_data(path:pd.DataFrame) -> pd.DataFrame:
#     df = pd.read_excel(path,skiprows=3)

#     first_col = df.columns[0]
#     if df[first_col].isnull().any():
#         df = df.drop(columns=first_col)
    
#     df = df.fillna(method='ffill')

#     return df


# def mrfp_vs_purchase_report(mrfp_data:pd.DataFrame,purchase_data:pd.DataFrame):
#     mrfp = clean_data(mrfp_data)
#     purchase = clean_data(purchase_data)




# a = mrfp_vs_purchase_report(path_mrfp,path_pur)
import os
from logging_config import logger
from datetime import date
import glob

end_date = date.today().strftime("%d-%m-%Y")


import os
import glob
import logging

# Set up logging (if not already set up)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_files(root_folder: str, end_date: str):
    # Print the root folder being processed
    print(f"Root folder: {root_folder}")
    
    # Define the search pattern for files with the specified end_date
    full_pattern = os.path.join(root_folder, "**", f"*{end_date}.xlsx")
    
    # Find and print each file that matches the pattern
    for file_path in glob.glob(full_pattern, recursive=True):
        try:
            # Print the file path
            print(f"Found file: {file_path}")
            logger.info(f"Found file: {file_path}")
            
            # Extract and print the report type
            report_type = file_path.split(os.sep)[-1].split('_')[1]
            print(f"Report type: {report_type}")
            
        except IndexError:
            # Handle cases where the filename format is incorrect
            logger.error(f"Invalid file path format: {file_path}")
            print(f"Invalid file path format: {file_path}")

# Example usage
process_files(r"D:\UserProfile\Desktop\data", end_date=end_date)


