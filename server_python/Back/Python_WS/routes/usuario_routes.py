from fastapi import APIRouter, HTTPException, Depends 
from models.usuario_model import Usuario
from schemas.usuario_schema import UsuarioCreateBaseModel
from schemas.usuario_schema import UsuarioUpdateBaseModel
from schemas.usuario_schema import UsuarioValidateBaseModel
from schemas.cliente_schema import ValidarVentaBaseModel
from schemas.inventario_schema import InventarioVentaBaseModel

from connection.connection import database
import re
import random, string
usuario = APIRouter()
# ESTA PARTE CORRESPONDE AL CRUD COMPLETO SOBRE UNA TABLA.
@usuario.post('/usuario/', tags=['usuario_ciberlynx'])
async def crear_usuario(usuario: UsuarioCreateBaseModel):
    usuario = Usuario.create(
        clv_usuario = usuario.clv_usuario,    
        nombre = usuario.nombre,
        usuario_nombre = usuario.usuario_nombre,
        contrasenia = usuario.contrasenia,
        estatus = usuario.estatus,
        rol = usuario.rol
    )
    return usuario

@usuario.put('/usuario_update/{usuario_nombre}', tags=['usuario_ciberlynx'])
async def actualizar_usuario(usuario: UsuarioUpdateBaseModel, usuario_nombre: str):
    Usuario.update(
        nombre = usuario.nombre,
        usuario_nombre = usuario.usuario_nombre,
        contrasenia  = usuario.contrasenia,
        estatus = usuario.estatus,
        rol = usuario.rol).where(Usuario.usuario_nombre == usuario_nombre).execute()

@usuario.delete('/usuario_delete/{usuario_nombre}', tags=['usuario_ciberlynx'])
async def eliminar_usuario(usuario_nombre: str):
    usuario = Usuario.get(Usuario.usuario_nombre == usuario_nombre)
    usuario.delete_instance()

@usuario.get('/usuario/{usuario_nombre}', tags=['usuario_ciberlynx'])
async def obtener_usuario(usuario_nombre:str):
    usuario = Usuario.get(Usuario.usuario_nombre == usuario_nombre)
    return usuario

@usuario.get('/usuario', tags=['usuario_ciberlynx'])
async def obtener_usuarios():
    usuarios = Usuario.select()
    return list(usuarios)

# Ruta para validar usuario y contraseña
@usuario.post('/validar_usuario/', tags=['usuario_ciberlynx'])
async def validar_usuario(usuario_validar: UsuarioValidateBaseModel):
    
    try:
        usuario = Usuario.get((Usuario.usuario_nombre == usuario_validar.usuario_nombre) & (Usuario.contrasenia == usuario_validar.contrasenia))

        with database.atomic():        
            folio_sesion = generar_clave()
            database.execute_sql(
                "CALL insertar_sesion(%s, %s, %s)",
                (folio_sesion, usuario.clv_usuario, 'Activo')
            )
        return {
            'folio_sesion': folio_sesion,
        }

    except Usuario.DoesNotExist:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

@usuario.post('/Venta/{insertar_venta}', tags=['usuario_ciberlynx'])
async def insertar_venta(cliente_validar: ValidarVentaBaseModel):
    with database.atomic():
        folio_venta = generar_clave()
        database.execute_sql(
            "CALL insertaventa(%s, %s)",
            (folio_venta, cliente_validar.clv_cliente)
        )

@usuario.post('/Detalle_Venta/{insertar_detalle}', tags=['usuario_ciberlynx'])
async def insertar_detalle_venta(detalle_venta : InventarioVentaBaseModel, venta: str, cantidad: float):
    with database.atomic():
        folio_detalle = generar_clave()
        database.execute_sql(
            "CALL inserta_Detalle_Venta(%s,%s,%s,%s,%s)",
            (folio_detalle,venta, detalle_venta.codigo_barras, cantidad, detalle_venta.precio)
        )

@usuario.get('/Consultar_Detalles/{Consulta}', tags=['usuario_ciberlynx'])
async def consultar_detalles(folio_venta: str):
    with database.atomic():
        database.execute_sql(
            "CALL consultar_detalles(%s)",(folio_venta)
        )

@usuario.delete('/Eliminar_Detalles/{Eliminar}', tags=['usuario_ciberlynx'])
async def eliminar_detalles(folio_detalle_venta: str):
    with database.atomic():
        database.execute_sql(
            "CALL eliminar_detalles(%s)",(folio_detalle_venta)
        )









def generar_clave():
    # Tomamos mayusculas, minusculas y digitos.
    caracteres = string.ascii_letters + string.digits
    # De acuerdo a la longitud de la clave.
    longitud_clave = 5
    # Toma de manera aleatoria 5 caracteres y los une en una sola cadena.
    clave = ''.join(random.choice(caracteres) for _ in range(longitud_clave))

    return clave  
