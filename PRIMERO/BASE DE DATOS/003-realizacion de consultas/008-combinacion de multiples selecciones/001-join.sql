- Create the user
CREATE USER 'miempresa'@'localhost' IDENTIFIED BY 'miempresa';

-- Grant all privileges on the database 'miempresa' to the user
GRANT ALL PRIVILEGES ON miempresa.* TO 'miempresa'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;