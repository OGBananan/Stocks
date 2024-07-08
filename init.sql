
CREATE DATABASE IF NOT EXISTS ${DB_NAME};

USE ${DB_NAME};

-- User Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Sample Data
INSERT INTO users (username, password, email)
VALUES ('admin', 'adminpassword', 'admin@example.com');
