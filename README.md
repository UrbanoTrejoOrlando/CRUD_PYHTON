# CRUD_PYHTON
## Descripción 
**API-TASK** es un Crud realizado en python utilizando el framewrok de FastApi  que permite la gestión de usuarios, implementando operaciones CRUD (Crear, Leer, Actualizar y Eliminar).
## Funcionalidades

- **CREATE**: Permite crear un nuevo usuario. 
- **READ**: Obtiene la lista completa de los usuarios o uno en especifico.
- **UPDATE**: Permite modificar los detalles de un usuario existente. 
- **DELETE**: Elimina un usuario por su clave. 

## Tecnologías utilizadas
- Python 
- FastApi  
- Mariadb o MySQL  

## Requisitos previos
Antes de ejecutar la API, asegúrate de tener una base de datos disponible. Puedes usar **MariaDB** o **MySQL**. A continuación, se detallan los pasos para instalar y configurar MariaDB:

### 1. Instalar MariaDB (en Archcraft o Arch Linux)

```bash
sudo pacman -S mariadb
```
### 2. Habilitar y arrancar el servicio
```bash
sudo systemctl status mariadb
sudo systemctl start mariadb
sudo systemctl enable mariadb
```
### 3. Configurar MariaDB (opcional pero recomendado)
```bash
sudo mysql_secure_installation
```
### 4. Crear la base de datos y el usuario
```bash
mysql -u root -p
```
Dentro del cliente de MariaDB:
```bash
CREATE DATABASE crud_python;
CREATE USER 'python'@'%' IDENTIFIED BY 'database';
GRANT ALL PRIVILEGES ON crud_python.* TO 'python'@'%';
FLUSH PRIVILEGES;
```
Ingresa a la base de datos con el usuario y contraseña que se creo
```bash
mysql -u python -p
show databases
use crud_python
```

