import pandas
from ventas_etl.transform.validate_schema import validate_columns

def test_validate_columns_missing_column():
    column_expected = ['Customer ID', 'Purchase Date', 'Product Category', 'Product Price',
    'Quantity', 'Total Purchase Amount', 'Payment Method', 'Customer Age', 'Returns',
    'Customer Name', 'Age', 'Gender', 'Churn']
    df_actual = pandas.DataFrame(columns=column_expected[:-1])
    resultado = validate_columns(df_actual, column_expected)
    assert resultado == (False, {"Churn"})

def test_validate_columns_valid():
        column_expected = ['Customer ID', 'Purchase Date', 'Product Category', 'Product Price',
        'Quantity', 'Total Purchase Amount', 'Payment Method', 'Customer Age', 'Returns',
        'Customer Name', 'Age', 'Gender', 'Churn']
        df_actual = pandas.DataFrame(columns=column_expected)
        resultado = validate_columns(df_actual, column_expected)
        assert resultado == (True, set())
