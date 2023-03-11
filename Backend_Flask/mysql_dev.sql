-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS flaskDb;
CREATE USER IF NOT EXISTS 'flask'@'localhost' IDENTIFIED BY 'flask_pwd';
GRANT ALL PRIVILEGES ON `flaskDb`.* TO 'flask'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'flask'@'localhost';

FLUSH PRIVILEGES;
