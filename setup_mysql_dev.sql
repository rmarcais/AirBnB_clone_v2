-- This script prepares a MySQL server for the project.
-- Create the database hbnb_dev_db.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Set all privileges.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
