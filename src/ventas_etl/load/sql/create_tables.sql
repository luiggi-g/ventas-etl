CREATE TABLE purchases (
    purchase_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id integer,
    purchase_date TIMESTAMP,
    product_category VARCHAR,
    product_price NUMERIC,
    quantity INTEGER,
    total_purchase_amount NUMERIC,
    payment_method VARCHAR,
    customer_age INTEGER,
    returns BOOLEAN,
    customer_name VARCHAR,
    gender VARCHAR,
    churn BOOLEAN
);