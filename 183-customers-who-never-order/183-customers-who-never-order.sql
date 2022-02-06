# Write your MySQL query statement below
SELECT name AS customers 
FROM customers WHERE ID Not In (SELECT customerId from orders);