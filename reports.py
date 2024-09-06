import pandas as pd

path_pur = r"D:\UserProfile\Desktop\purchase.xlsx"
path_mrfp = r"D:\UserProfile\Desktop\mrfp.xlsx"
def clean_data(path:pd.DataFrame) -> pd.DataFrame:
    df = pd.read_excel(path,skiprows=3)

    first_col = df.columns[0]
    if df[first_col].isnull().any():
        df = df.drop(columns=first_col)
    
    df = df.fillna(method='ffill')

    return df


def mrfp_vs_purchase_report(mrfp_data:pd.DataFrame,purchase_data:pd.DataFrame):
    mrfp = clean_data(mrfp_data)
    purchase = clean_data(purchase_data)




a = mrfp_vs_purchase_report(path_mrfp,path_pur)
print(a)


