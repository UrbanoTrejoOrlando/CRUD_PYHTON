from pydantic import BaseModel
from typing import Optional

class SesionBaseModel(BaseModel):
    folio_sesion: str
    clv_usuario: str
    estado: str
    fecha: DateTimeField = DateTimeField(default=datetime.datetime.now())
