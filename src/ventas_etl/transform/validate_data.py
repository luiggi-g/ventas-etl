from pathlib import Path
import json
import pandas as pd
from ventas_etl.config.read_json import read_json_config

def get_validation_rules():
    return read_json_config("ecommerce_schema.json")

def validate_nulls(df_actual: pd.DataFrame,validation_rules: dict):
    nullable_columns = validation_rules["nullable_columns"]
    null_columns = list(df_actual.columns[df_actual.isnull().any()])
    invalid_null_columns = set(null_columns) - set(nullable_columns)
    if invalid_null_columns:
        nulls_is_valid = False
    else:
        nulls_is_valid = True
    return nulls_is_valid,invalid_null_columns

def validate_dtypes(df_actual: pd.DataFrame,validation_rules:dict):
    column_types = validation_rules["column_types"]
    df_actual_dtypes = df_actual.dtypes.astype(str).to_dict()
    invalid_dtypes = {}
    for column in df_actual.columns:
        types_expected = column_types[column]
        if types_expected != df_actual_dtypes[column]:
            invalid_dtypes[column] = {
            "expected": types_expected,
            "actual": df_actual_dtypes[column]
        }
    dtypes_is_valid = not invalid_dtypes
    return dtypes_is_valid, invalid_dtypes

def validate_allowed_values(df_actual:pd.DataFrame,validation_rules:dict):
    allowed_values = validation_rules["allowed_values"]
    invalid_values = {}
    for column, values  in allowed_values.items():
        if column in df_actual.columns:
            invalid_rows = df_actual[df_actual[column].notna() &~df_actual[column].isin(values)]

            if not invalid_rows.empty:
                invalid_values[column] = invalid_rows[column].unique().tolist()

    values_is_valid = not invalid_values
    return values_is_valid, invalid_values


def validate_data(df_actual):
    validation_rules = get_validation_rules()
    nulls_is_valid,invalid_null_columns = validate_nulls(df_actual,validation_rules)
    dtypes_is_valid,invalid_dtypes = validate_dtypes(df_actual,validation_rules)
    values_is_valid, invalid_values = validate_allowed_values(df_actual,validation_rules)
    data_is_valid = nulls_is_valid and dtypes_is_valid and values_is_valid
    return data_is_valid,invalid_null_columns, invalid_dtypes , invalid_values
