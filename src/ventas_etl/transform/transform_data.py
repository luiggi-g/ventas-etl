import pandas as pd
from src.ventas_etl.config.read_json import read_json_config

def get_transform_rules():
    return read_json_config("ecommerce_transform.json")


def transform_datetime(df_actual):
    df_actual["Purchase Date"]= pd.to_datetime(df_actual["Purchase Date"])
    return df_actual

def transform_boolean_columns(df_actual):
   df_actual['Returns'] = df_actual['Returns'].apply(lambda x: bool(x) if pd.notna(x) else None)
   df_actual['Churn'] = df_actual['Churn'].astype(bool)

   return df_actual

def remove_redundant_columns(df_actual,transform_rules):
    redundant_columns = transform_rules["redundant_columns"]
    for column in redundant_columns:
        df_actual = df_actual.drop(columns=[column])
    return df_actual



def transform_data(df_actual):
    transform_rules = get_transform_rules()
    df_actual = transform_datetime(df_actual)
    df_actual = remove_redundant_columns(df_actual,transform_rules)
    df_actual = transform_boolean_columns(df_actual)
    return df_actual
