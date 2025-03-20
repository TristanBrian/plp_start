USE SalesDB;

DROP TABLE IF EXISTS SalesDB.Products;

CREATE TABLE SalesDB.Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/*  inserting values to table*/

INSERT INTO SalesDB.Products (ProductName, Price) VALUES
( 'Laptop', '500.00'),
( 'Tablet', '200.00'),
('Smartphone' , '300.00'),
('Television', '700.00'),
('Subwoofer', '900.00');

/*  selecting where price is greater than 500 (used wildcards for flexible searching)*/
SELECT * FROM SalesDB.Products WHERE PRICE > 500 AND ProductName = 'Laptop';

/*  selecting to order by price*/
SELECT * FROM SalesDB.Products ORDER BY Price DESC;
SELECT * FROM SalesDB.Products ORDER BY Price ASC;

/*  selecting where product name has this spelling {l}*/
SELECT * FROM SalesDB.Products WHERE ProductName LIKE 'L%';
SELECT * FROM SalesDB.Products WHERE ProductName LIKE '%S%';

/*  updating a product*/
UPDATE Products
SET Category = 'Stationery'
WHERE Category = 'Stationary';

/*  Truncating a table*/
TRUNCATE TABLE SalesDB.Products;
