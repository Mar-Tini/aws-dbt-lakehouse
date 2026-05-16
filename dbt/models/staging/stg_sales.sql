SELECT
    invoice_no,
    stock_code,
    quantity,
    invoice_date,
    unit_price,
    country,
    quantity * unit_price AS revenue
FROM raw_orders
WHERE quantity IS NOT NULL
  AND unit_price IS NOT NULL
  AND quantity > 0
  AND unit_price > 0