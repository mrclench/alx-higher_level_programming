--  Script to CREATE a table "unique_id" with description
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)
-- script shouldnt fail if table already exists
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
