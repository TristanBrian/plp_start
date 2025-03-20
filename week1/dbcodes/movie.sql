/*Build and query a simple database about movies, actors.

Create two tables: Movies  and Actors. */
CREATE DATABASE IF NOT EXISTS MovieDB;
USE MovieDB;

CREATE TABLE Movies (
    Movieid INT PRIMARY KEY AUTO_INCREMENT,
    Moviename VARCHAR(255) NOT NULL,
    movieyear INT NOT NULL,
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Actors (
    Actorid INT PRIMARY KEY AUTO_INCREMENT,
    Actorname VARCHAR(255) NOT NULL,
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/*  inserting values to table*/
INSERT INTO Movies (Moviename, movieyear) VALUES
( 'The Matrix', 1999),
( 'The Matrix Reloaded', 2003),
('The Matrix Revolutions' , 2003),
('The Lord of the Rings: The Fellowship of the Ring', 2001),
('The Lord of the Rings: The Two Towers', 2002),
('The Lord of the Rings: The Return of the King', 2003);

INSERT INTO Actors (Actorname) VALUES
( 'Keanu Reeves'),
( 'Laurence Fishburne'),
('Carrie-Anne Moss'),
('Hugo Weaving'),
('Ian McKellen'),
('Viggo Mortensen');
/*  Querying the database*/
SELECT * FROM Movies;
SELECT * FROM Actors;
SELECT * FROM Movies WHERE movieyear = 2003;
SELECT * FROM Actors WHERE Actorname LIKE 'K%';
SELECT * FROM Movies WHERE Moviename LIKE '%Matrix%';
SELECT * FROM Actors WHERE Actorname LIKE '%M%';
SELECT * FROM Movies ORDER BY movieyear DESC;
SELECT * FROM Actors ORDER BY Actorname ASC;
UPDATE Movies
SET movieyear = 2000
WHERE movieyear = 2001;

