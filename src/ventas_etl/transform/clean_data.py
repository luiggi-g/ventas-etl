import pandas as pd
from ventas_etl.config.read_json import read_json_config

def get_cleaning_rules():
    return read_json_config("ecommerce_cleaning.json")

def clean_strings(df_actual, cleaning_rules):
    strip_strings = cleaning_rules["strip_strings"]
    for column in strip_strings:
        df_actual[column] = df_actual[column].str.strip()
    return df_actual

def clean_duplicates(df_actual: pd.DataFrame, cleaning_rules):
    remove_duplicates = cleaning_rules["remove_duplicates"]

    if remove_duplicates:
        df_actual = df_actual.drop_duplicates()

    return df_actual

def clean_data(df_actual):
    cleaning_rules=get_cleaning_rules()
    df_actual = clean_strings(df_actual,cleaning_rules)
    df_actual = clean_duplicates(df_actual,cleaning_rules)

    return df_actual