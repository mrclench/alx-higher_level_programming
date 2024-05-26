-- This script creates a database names 'hbtn_0d_usa' and creates 
-- table 'states' in the 'hbtn_0d_usa' database
-- 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
