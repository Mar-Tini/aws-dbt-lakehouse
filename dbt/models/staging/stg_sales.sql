SELECT
    invoice_no,
    stock_code,
    CAST(quantity AS INTEGER) AS quantity,
    invoice_date,
    CAST(unit_price AS NUMERIC) AS unit_price,
    country,
    quantity * unit_price AS revenue

FROM {{ source('ecommerce', 'raw_orders') }}

WHERE quantity IS NOT NULL
  AND unit_price IS NOT NULL
  AND quantity > 0
  AND unit_price > 0