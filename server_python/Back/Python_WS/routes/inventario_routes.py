from fastapi import APIRouter, HTTPException
from models.inventario_model import Inventario
from schemas.inventario_schema import InventarioCreateBaseModel
from schemas.inventario_schema import InventarioUpdateBaseModel

from connection.connection import database

import random, string
inventario = APIRouter()

@inventario.post('/inventario', tags=['inventario_ciberlynx'])
async def crear_inventario(inventario: InventarioCreateBaseModel):
    inventario = Inventario.create(
        codigo_barras = inventario.codigo_barras,
        nombre = inventario.nombre,
        descripcion = inventario.descripcion,
        precio = inventario.precio,
        marca = inventario.marca,
        categoria = inventario.categoria,
        stock = inventario.stock,
        Unidad_Medida = inventario.Unidad_Medida
    )  
    return inventario

@inventario.put('/inventario_update/{nombre}', tags=['inventario_ciberlynx'])
async def actualizar_inventario(inventario: InventarioUpdateBaseModel, nombre: str):
    Inventario.update(
        nombre = inventario.nombre,
        descripcion = inventario.descripcion,
        marca = inventario.marca).where(Inventario.nombre == nombre).execute()

@inventario.delete('/inventario_delete/{nombre}', tags=['inventario_ciberlynx'])
async def eliminar_inventario(nombre: str):
    inventario = Inventario.get(Inventario.nombre == nombre)
    inventario.delete_instance()

@inventario.get('/inventario/{nombre}',tags=['inventario_ciberlynx'])
async def obtener_inventario(nombre: str):
    inventario = Inventario.get(Inventario.nombre == nombre)
    return inventario

@inventario.get('/inventarios', tags=['inventario_ciberlynx'])
async def obtener_inventarios():
    inventario = Inventario.select()
    return list(inventario)

