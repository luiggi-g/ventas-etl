
import pandas as pd
from unittest.mock import MagicMock

from ventas_etl.load.load_data import insert_batch


def test_insert_batch_executes_query_with_12_parameters():
    batch = pd.DataFrame(
        [
            {
                "customer_id": 101,
                "purchase_date": pd.Timestamp("2025-01-15"),
                "product_category": "Electronics",
                "product_price": 120.50,
                "quantity": 2,
                "total_purchase_amount": 241.00,
                "payment_method": "Credit Card",
                "customer_age": 30,
                "returns": False,
                "customer_name": "Juan",
                "gender": "Male",
                "churn": False,
            }
        ]
    )

    connection = MagicMock()
    cursor = connection.cursor.return_value.__enter__.return_value

    insert_batch(connection, batch)

    cursor.executemany.assert_called_once()
    query, rows = cursor.executemany.call_args.args
    rows = list(rows)

    assert query.count("%s") == 12

    assert len(rows) == 1
    assert len(rows[0]) == 12

    connection.commit.assert_not_called()
