from fastapi import APIRouter, HTTPException, Depends
from schemas.cliente_schema import ValidarVentaBaseModel

from connection.connection import database
import random, string
venta = APIRouter()

@venta.post('/Venta/{insertar_venta}', tags=['usuario_ciberlynx'])
async def insertar_venta(cliente_validar: ValidarVentaBaseModel):
    with database.atomic():
        folio_venta = generar_clave()
        database.execute_sql(
            "CALL insertaventa(%s, %s)",
            (folio_venta, cliente_validar.clv_cliente)
        )


def generar_clave():
    # Tomamos mayusculas, minusculas y digitos.
    caracteres = string.ascii_letters + string.digits
    # De acuerdo a la longitud de la clave.
    longitud_clave = 5
    # Toma de manera aleatoria 5 caracteres y los une en una sola cadena.
    clave = ''.join(random.choice(caracteres) for _ in range(longitud_clave))

    return clave

