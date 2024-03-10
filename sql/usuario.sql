CREATE DATABASE crud_python;
CREATE USER 'python'@'%' IDENTIFIED BY 'database';
GRANT ALL PRIVILEGES ON crud_python.* TO 'python'@'%';
FLUSH PRIVILEGES;

