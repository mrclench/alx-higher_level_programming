-- This script creates database hbtn_0d_2 and also creates a user 
-- user_0d_2.
-- Notes:
-- Should only have the SELECT privilege in database hbtn_0d_2
-- password for user will be user_0d_2_pwd and script should fail if any exists .
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
