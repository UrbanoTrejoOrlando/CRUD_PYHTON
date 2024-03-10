from pydantic import BaseModel
from typing import Optional

class PersonaCreateBaseModel(BaseModel):
    clv_persona: str
    nombre: str 
    apellido_p: str
    apellido_m: str
    usuario_nombre: str
    contrasenia: str
    edad: float

class PersonaUpdateBaseModel(BaseModel):
    nombre: str
    apellido_p: str
    apellido_m: str
    usuario_nombre: str
    contrasenia: str
    edad: float

