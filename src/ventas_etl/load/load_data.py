import os
from dotenv import load_dotenv
import psycopg
from ventas_etl.config.read_json import read_json_config


def get_load_rules():
    return read_json_config("ecommerce_load.json")


def get_credentials():
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    return db_host, db_port, db_name, db_user, db_password


def get_connection(db_host, db_port, db_name, db_user, db_password):
    return psycopg.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password,
        port=db_port
    )


def split_into_batches(df_actual, load_rules):
    batch_size = load_rules["batch_size"]

    for i in range(0, len(df_actual), batch_size):
        yield df_actual.iloc[i:i + batch_size]


def insert_batch(connection, batch):
    batch = batch.itertuples(index=False, name=None)

    query = """
        INSERT INTO purchases (
            customer_id,
            purchase_date,
            product_category,
            product_price,
            quantity,
            total_purchase_amount,
            payment_method,
            customer_age,
            returns,
            customer_name,
            gender,
            churn
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s
            )
    """

    with connection.cursor() as cur:
        cur.executemany(query, batch)

def load_data(df_actual):
    load_rules = get_load_rules()

    db_host, db_port, db_name, db_user, db_password = get_credentials()

    with get_connection(db_host,db_port,db_name,db_user,db_password) as connection:
        for lot_num, lot in enumerate(
            split_into_batches(df_actual, load_rules),
            start=1
        ):
            try:
                insert_batch(connection, lot)
                connection.commit()

            except Exception as e:
                connection.rollback()
                print(f"ERROR en batch {lot_num}: {e}")
                raise