SELECT
    invoice_date::date AS order_date,
    country,

    COUNT(DISTINCT invoice_no) AS total_orders,

    SUM(quantity) AS total_quantity,

    SUM(revenue) AS total_revenue,

    AVG(revenue) AS average_order_value

FROM {{ ref('stg_sales') }}

GROUP BY 1, 2