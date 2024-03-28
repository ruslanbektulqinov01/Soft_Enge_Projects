SELECT products.product_name AS "Product Name",
       categories.category_name AS "Category Name",
       COUNT(order_details.order_id) AS "Number of Orders",
       SUM(order_details.quantity) AS "Total Quantity",
       SUM(order_details.unit_price * order_details.quantity) AS "Total Revenue"
FROM order_details
JOIN products ON order_details.product_id = products.product_id
JOIN categories ON products.category_id = categories.category_id
GROUP BY products.product_name, categories.category_name
ORDER BY "Number of Orders" DESC;