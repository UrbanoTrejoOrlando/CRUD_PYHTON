# Author: Orlando Urbano Trejo
# Email: orlandourbanotrejo@gmail.com
# Date:  02-26-2024
from peewee import *

# Establishes the credentials for accessing the database
database = MySQLDatabase('crud_python', 
                        user='python', 
                        password='database',
                        host='localhost',
                        port=3306)
