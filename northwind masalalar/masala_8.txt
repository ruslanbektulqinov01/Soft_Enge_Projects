SELECT customer_id, company_name, SUM(quantity * unit_price) AS total_spent
FROM customers
JOIN orders USING (customer_id)
JOIN order_details USING (order_id)
WHERE EXTRACT(YEAR FROM order_date) = 1997
GROUP BY customer_id, company_name
ORDER BY total_spent DESC;