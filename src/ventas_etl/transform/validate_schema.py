from pathlib import Path
import json
import pandas as pd
from ventas_etl.config.read_json import read_json_config

def get_required_columns() -> list[str]:
    json_data = read_json_config("ecommerce_schema.json")
    required_columns = json_data["required_columns"]
    return required_columns

def validate_columns(df_actual: pd.DataFrame,required_columns: list[str]):
    df_columns = list(df_actual.columns)
    if sorted(required_columns) != sorted(df_columns):
        schema_is_valid = False
        set_required_columns = set(required_columns)
        set_df_actual = set(df_columns)
        different_elements = set_required_columns ^ set_df_actual
    else:
        schema_is_valid = True
        different_elements = set()
    return schema_is_valid,different_elements

#orquestador validate schema
def validate_schemas(df_actual):
    required_columns = get_required_columns()
    schema_is_valid,different_elements = validate_columns(df_actual,required_columns)
    return schema_is_valid,df_actual,different_elements
