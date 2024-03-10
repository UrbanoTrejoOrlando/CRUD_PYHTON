import os 
os.environ['PYTHONPATH'] = 'Python_WS/connection'

from connection.connection import database
from peewee import *

class Persona(Model):
    clv_persona = CharField(primary_key=True, max_length=5)
    nombre = CharField(max_length=50, null=False)
    apellido_p = CharField(max_length=50, null=False)
    apellido_m = CharField(max_length=50, null=False)
    usuario_nombre = CharField(max_length=20, null=False)
    contrasenia = CharField(max_length=10, null=False)
    edad = FloatField(null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        database = database
        table_name = 'persona'
