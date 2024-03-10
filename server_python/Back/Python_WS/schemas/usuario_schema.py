from pydantic import BaseModel
from typing import Optional

class UsuarioCreateBaseModel(BaseModel):
    clv_usuario: str
    nombre: str
    usuario_nombre: str
    contrasenia: str
    estatus: Optional[str] = 'ACTIVO'
    rol: Optional[str] = 'Empleado'

class UsuarioUpdateBaseModel(BaseModel):
    nombre: str
    usuario_nombre: str
    contrasenia: str
    estatus: Optional[str] = 'ACTIVO'
    rol: Optional[str] = 'Empleado'

class UsuarioValidateBaseModel(BaseModel):    
    usuario_nombre: str
    contrasenia:str

