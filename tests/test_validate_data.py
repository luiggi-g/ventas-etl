import pandas
from ventas_etl.transform.validate_data import validate_nulls
from ventas_etl.transform.validate_data import get_validation_rules
from ventas_etl.transform.validate_data import validate_dtypes
from ventas_etl.transform.validate_data import validate_allowed_values
from ventas_etl.transform.validate_data import validate_data

def test_validate_nulls ():
    df_actual= pandas.DataFrame({
        "Customer ID": [1,2],
        "Returns": [1.0,None]
    })
    validation_rules = get_validation_rules()
    resultado = validate_nulls(df_actual,validation_rules)
    assert resultado == (True,set())

def test_validate_nulls_invalid_column():
    df_actual= pandas.DataFrame({
        "Customer ID": [1,None],
        "Returns": [1.0,None]
    })
    validation_rules = get_validation_rules()
    resultado = validate_nulls(df_actual,validation_rules)
    assert resultado == (False,{"Customer ID"})

def test_validate_dtypes_valid():
    df_actual= pandas.DataFrame({
        "Customer ID": pandas.Series([1,2],dtype="int64"),
        "Product Price": pandas.Series([100, 200], dtype="int64"),
    })
    validation_rules = get_validation_rules()
    resultado = validate_dtypes(df_actual, validation_rules)
    assert resultado == (True,{})

def test_validate_dtypes_invalid():
    df_actual= pandas.DataFrame({
        "Customer ID": pandas.Series([1,2],dtype="str"),
        "Product Price": pandas.Series([100, 200], dtype="int64"),
    })
    validation_rules = get_validation_rules()
    resultado = validate_dtypes(df_actual, validation_rules)
    assert resultado == (False,{ "Customer ID":{"expected": "int64","actual":"str"}})

def test_validate_allowed_values_valid():
    df_actual= pandas.DataFrame({
        "Customer ID": [1],
        "Churn":  [0],
        "Product Category": ["Electronics"]
    })
    validation_rules = get_validation_rules()
    resultado = validate_allowed_values(df_actual,validation_rules)
    assert resultado == (True,{})

def test_validate_allowed_values_invalid():
    df_actual= pandas.DataFrame({
        "Customer ID": [1],
        "Churn":  [3],
        "Product Category": ["TV"]
    })
    validation_rules = get_validation_rules()
    resultado = validate_allowed_values(df_actual,validation_rules)
    assert resultado == (False,{"Churn": [3],"Product Category": ["TV"]})

def test_validate_data():
    df_actual = pandas.DataFrame({
    "Customer ID": pandas.Series([1, 2], dtype="int64"),
    "Purchase Date": ["2023-05-03 21:30:02", "2023-06-10 14:20:00"],
    "Product Category": ["Electronics", "Books"],
    "Product Price": pandas.Series([100, 200], dtype="int64"),
    "Quantity": pandas.Series([2, 1], dtype="int64"),
    "Total Purchase Amount": pandas.Series([250, 200], dtype="int64"),
    "Payment Method": ["Credit Card", "PayPal"],
    "Customer Age": pandas.Series([25, 34], dtype="int64"),
    "Returns": pandas.Series([1.0, None], dtype="float64"),
    "Customer Name": ["Juan", "Pedro"],
    "Age": pandas.Series([25, 34], dtype="int64"),
    "Gender": ["Male", "Female"],
    "Churn": pandas.Series([0, 1], dtype="int64")
    })
    resultado = validate_data(df_actual)
    assert resultado == (True, set(), {}, {})

def test_validate_data_invalid():
    df_actual = pandas.DataFrame({
    "Customer ID": pandas.Series([1, 2], dtype="int64"),
    "Purchase Date": ["2023-05-03 21:30:02", "2023-06-10 14:20:00"],
    "Product Category": ["Electronics", "Books"],
    "Product Price": pandas.Series([100, 200], dtype="int64"),
    "Quantity": pandas.Series([2, 1], dtype="int64"),
    "Total Purchase Amount": pandas.Series([250, 200], dtype="int64"),
    "Payment Method": ["Credit Card", "PayPal"],
    "Customer Age": pandas.Series([25, 34], dtype="int64"),
    "Returns": pandas.Series([1.0, None], dtype="float64"),
    "Customer Name": ["Juan", "Pedro"],
    "Age": pandas.Series([25, 34], dtype="int64"),
    "Gender": ["Male", "Female"],
    "Churn": pandas.Series([0, 3], dtype="int64")
    })
    resultado = validate_data(df_actual)
    assert resultado == (False, set(), {}, {"Churn": [3]})
