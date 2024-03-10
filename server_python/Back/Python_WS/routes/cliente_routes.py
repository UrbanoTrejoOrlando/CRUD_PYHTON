from fastapi import APIRouter, HTTPException
from models.cliente_model import Cliente
from schemas.cliente_schema import ClienteCreateBaseModel
from schemas.cliente_schema import ClienteUpdateBaseModel
from schemas.cliente_schema import ValidarVentaBaseModel

from connection.connection import database

import random, string
cliente = APIRouter()

@cliente.post('/cliente', tags=['cliente_ciberlynx'])
async def crear_cliente(cliente: ClienteCreateBaseModel):
    cliente = Cliente.create(
        clv_cliente = cliente.clv_cliente,
        nombre = cliente.nombre,
        alias = cliente.alias,
        direccion = cliente.direccion,
        estado = cliente.estado,
        telefono = cliente.telefono
    )
    return cliente

@cliente.put('/cliente_update{nombre}', tags=['cliente_ciberlynx'])
async def actualizar_cliente(cliente: ClienteUpdateBaseModel, nombre: str):
    Cliente.update(
        nombre = cliente.nombre,
        alias = cliente.alias,
        direccion = cliente.direccion,
        estado = cliente.estado,
        telefono = cliente.telefono).where(Cliente.nombre == nombre).execute()

@cliente.delete('/cliente_delete/{nombre}', tags=['cliente_ciberlynx'])
async def eliminar_cliente(nombre: str):
    cliente = Cliente.get(Cliente.nombre == nombre)
    cliente.delete_instance()

@cliente.get('/cliente/{nombre}', tags=['cliente_ciberlynx'])
async def obtener_cliente(nombre: str):
    cliente = Cliente.get(Cliente.nombre == nombre)
    return cliente

@cliente.get('/cliente', tags=['cliente_ciberlynx'])
async def obtener_clientes():
    cliente = Cliente.select()
    return list(cliente)
