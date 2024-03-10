from fastapi import APIRouter, HTTPException
from models.persona_model import Persona
from schemas.persona_schema import PersonaCreateBaseModel
from schemas.persona_schema import PersonaUpdateBaseModel

from connection.connection import database

import random, string
persona = APIRouter()

@persona.post('/persona', tags=['persona_ejemplo'])
async def crear_persona(persona: PersonaCreateBaseModel):
    persona = Persona.create(
        clv_persona = persona.clv_persona,
        nombre = persona.nombre,
        apellido_p = persona.apellido_p,
        apellido_m = persona.apellido_m,
        usuario_nombre = persona.usuario_nombre,
        contrasenia = persona.contrasenia,
        edad = persona.edad
    )
    return persona

@persona.put('/persona_update', tags=['persona_ejemplo'])
async def actualizar_persona(persona: PersonaUpdateBaseModel, nombre: str):
    Persona.update(
        nombre = persona.nombre,
        apellido_p = persona.apellido_p,
        apellido_m = persona.apellido_m,
        usuario_nombre = persona.usuario_nombre,
        contrasenia = persona.contrasenia,
        edad = persona.edad).where(Persona.nombre == nombre).execute()

@persona.delete('/persona_delete/', tags=['persona_ejemplo'])
async def eliminar_persona(nombre: str):
    persona = Persona.get(Persona.nombre == nombre)
    persona.delete_instance()

@persona.get('/persona/{nombre}', tags=['persona_ejemplo'])
async def obtener_persona(nombre: str):
    persona = Persona.get(Persona.nombre == nombre)
    return persona

@persona.get('/persona', tags=['persona_ejemplo'])
async def obtener_personas():
    persona = Persona.select()
    return list(persona)
