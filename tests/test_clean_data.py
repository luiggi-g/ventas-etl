import pandas
from ventas_etl.transform.clean_data import get_cleaning_rules
from ventas_etl.transform.clean_data import clean_strings
from ventas_etl.transform.clean_data import clean_duplicates
from ventas_etl.transform.clean_data import clean_data

def test_clean_strings_valid():
    df_actual = pandas.DataFrame({
        "Customer ID": pandas.Series([1, 2], dtype="int64"),
        "Product Category": ["Electronics", "Books"],
        "Payment Method": ["Credit Card", "PayPal"],
        "Customer Name": ["Juan", "Pedro"],
        "Gender": ["Male", "Female"],
    })
    cleaning_rules = get_cleaning_rules()
    resultado = clean_strings(df_actual,cleaning_rules)
    assert resultado["Product Category"].tolist() == ["Electronics", "Books"]
    assert resultado["Payment Method"].tolist() == ["Credit Card", "PayPal"]
    assert resultado["Customer Name"].tolist() == ["Juan", "Pedro"]
    assert resultado["Gender"].tolist() == ["Male", "Female"]

def test_clean_strings_strip_whitespace():
    df_actual = pandas.DataFrame({
        "Customer ID": pandas.Series([1, 2], dtype="int64"),
        "Product Category": ["Electronics ", " Books "],
        "Payment Method": ["Credit Card ", " PayPal "],
        "Customer Name": [" Juan", "Pedro "],
        "Gender": ["Male ", "Female "],
    })
    cleaning_rules = get_cleaning_rules()
    resultado = clean_strings(df_actual,cleaning_rules)
    assert resultado["Product Category"].tolist() == ["Electronics", "Books"]
    assert resultado["Payment Method"].tolist() == ["Credit Card", "PayPal"]
    assert resultado["Customer Name"].tolist() == ["Juan", "Pedro"]
    assert resultado["Gender"].tolist() == ["Male", "Female"]

def test_clean_duplicates_valid():
    df_actual = pandas.DataFrame({
    "Customer ID": pandas.Series([1, 2], dtype="int64"),
    "Product Category": ["Electronics", "Books"],
    "Payment Method": ["Credit Card", "PayPal"],
    "Customer Name": ["Juan", "Pedro"],
    "Gender": ["Male", "Female"],
    })
    cleaning_rules = get_cleaning_rules()
    resultado = clean_duplicates(df_actual,cleaning_rules)
    assert len(df_actual) == len(resultado)
    pandas.testing.assert_frame_equal(resultado, df_actual)


def test_clean_duplicates_remove_duplicates():
    df_actual = pandas.DataFrame({
    "Customer ID": pandas.Series([1, 1], dtype="int64"),
    "Product Category": ["Electronics", "Electronics"],
    "Payment Method": ["Credit Card", "Credit Card"],
    "Customer Name": ["Juan", "Juan"],
    "Gender": ["Male", "Male"],
    })
    cleaning_rules = get_cleaning_rules()
    resultado = clean_duplicates(df_actual,cleaning_rules)
    assert len(df_actual) != len(resultado)
    assert resultado["Customer ID"].tolist() == [1]

def test_clean_data_valid():
    df_actual = pandas.DataFrame({
        "Customer ID": pandas.Series([1, 2], dtype="int64"),
        "Product Category": ["Electronics", "Books"],
        "Payment Method": ["Credit Card", "PayPal"],
        "Customer Name": ["Juan", "Pedro"],
        "Gender": ["Male", "Female"],
    })
    cleaning_rules = get_cleaning_rules()
    resultado = clean_data(df_actual)
    assert resultado["Product Category"].tolist() == ["Electronics", "Books"]
    assert resultado["Payment Method"].tolist() == ["Credit Card", "PayPal"]
    assert resultado["Customer Name"].tolist() == ["Juan", "Pedro"]
    assert resultado["Gender"].tolist() == ["Male", "Female"]
    assert len(df_actual) == len(resultado)

def test_clean_data_remove_strip():
    df_actual = pandas.DataFrame({
        "Customer ID": pandas.Series([1, 1], dtype="int64"),
        "Product Category": ["Books ", "Books "],
        "Payment Method": [" Credit Card ", " Credit Card "],
        "Customer Name": ["Juan ", "Juan "],
        "Gender": ["Male ", "Male "],
    })
    cleaning_rules = get_cleaning_rules()
    resultado = clean_data(df_actual)
    assert resultado["Product Category"].tolist() == ["Books"]
    assert resultado["Payment Method"].tolist() == ["Credit Card"]
    assert resultado["Customer Name"].tolist() == ["Juan"]
    assert resultado["Gender"].tolist() == ["Male"]
    assert len(df_actual) != len(resultado)
