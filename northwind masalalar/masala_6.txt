SELECT employees.employee_id AS "Employee ID",
       employees.first_name | |  ' '   | |employees.last_name AS "Employee Name",
       COUNT(orders.order_id) AS "Number of Orders",
       SUM(order_details.quantity) AS "Total Quantity Sold",
       SUM(order_details.unit_price * order_details.quantity) AS "Total Revenue"
FROM employees
JOIN orders ON employees.employee_id = orders.employee_id
JOIN order_details ON orders.order_id = order_details.order_id
WHERE employees.country = 'USA'
GROUP BY employees.employee_id, employees.first_name, employees.last_name
ORDER BY "Number of Orders" DESC;