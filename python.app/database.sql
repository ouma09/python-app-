-- SQL script to create the database and table
CREATE DATABASE IF NOT EXISTS calculations;
USE your_database_name;

CREATE TABLE IF NOT EXISTS calculation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    num1 FLOAT,
    num2 FLOAT,
    result FLOAT
);
