USE SalesDB;

DROP TABLE IF EXISTS SalesDB.Products;

CREATE TABLE SalesDB.Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL
);

/*  inserting values to table*/

INSERT INTO SalesDB.Products (ProductName, Price) VALUES
( 'Laptop', '500.00'),
( 'Tablet', '200.00'),
('Smartphone' , '300.00'),
('Television', '700.00');


/*  selecting where price is greater than 500*/
SELECT * FROM SalesDB.Products WHERE PRICE > 500;

/*  selecting to order by price*/
SELECT * FROM SalesDB.Products ORDER BY Price DESC;

/*  selecting where product name has this spelling {l}*/
SELECT * FROM SalesDB.Products WHERE ProductName LIKE 'L%';
SELECT * FROM SalesDB.Products WHERE ProductName LIKE '%S%';

/*  updating a product*/
UPDATE Products
SET Category = 'Stationery'
WHERE Category = 'Stationary';

 /*  Truncating a table*/
 TRUNCATE TABLE SalesDB.Products;



