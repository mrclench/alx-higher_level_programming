-- A script to CREATE a table id_not_null and in table
-- id INT with default value 1
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256) NOT NULL
);
