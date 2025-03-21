/*Write an SQL query to retrieve the checkNumber, paymentDate, and amount from the payments table.*/

SELECT checkNumber, paymentDate, amount from payments;


Write an SQL query to retrieve the orderDate, requiredDate, and status of orders that are currently 'In Process' from the orders table. Sort the results in descending order of orderDate

SELECT orderDate, requiredDate, status from orders where status = 'In Process' order by orderDate desc;

Write a query to display the firstName, lastName, and email of employees whose job title is 'Sales Rep' and order them in descending order of employeeNumber.


SELECT firstName, lastName, email from employees where jobTitle = 'Sales Rep' order by employeeNumber desc;


Write a query to retrieve all the columns and records from the offices table.

Write a query to fetch the productName and quantityInStock from the products table. Sort the results in ascending order of buyPrice and limit the output to 5 records.