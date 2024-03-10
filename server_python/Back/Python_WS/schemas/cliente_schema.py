from pydantic import BaseModel
from typing import Optional

class ClienteCreateBaseModel(BaseModel):
    clv_cliente: str
    nombre: str
    alias: str
    direccion: str
    estado: Optional[str] = 'ACTIVO'
    telefono: str

class ClienteUpdateBaseModel(BaseModel):
    nombre: str
    alias: str
    direccion: str
    estado: str
    telefono: str

class ValidarVentaBaseModel(BaseModel):
    clv_cliente: str
