-- This script prepares a MySQL server for the project.
-- Create the database hbnb_test_db.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Set all privileges.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
