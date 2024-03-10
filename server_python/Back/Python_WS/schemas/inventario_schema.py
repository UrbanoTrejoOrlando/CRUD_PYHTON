from pydantic import BaseModel
from typing import Optional

class InventarioCreateBaseModel(BaseModel):
    codigo_barras: str
    nombre: str
    descripcion: str
    precio: float
    marca: str
    categoria: str
    stock: float
    Unidad_Medida: str

class InventarioUpdateBaseModel(BaseModel):
    nombre: str
    descripcion: str
    marca: str

class InventarioVentaBaseModel(BaseModel):
    codigo_barras: str 
    precio: float
