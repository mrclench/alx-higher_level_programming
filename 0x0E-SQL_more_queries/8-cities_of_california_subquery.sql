-- A script thats lists all cities of California from the "hbtn_0d_usa" database
USE hbtn_0d_usa;

SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
