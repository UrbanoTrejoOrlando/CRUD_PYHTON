from fastapi import FastAPI

from routes.persona_routes import persona
from models.persona_model import Persona

from connection.connection import database as conexion
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title = 'Conexion',
    description = 'Establece una conexion a la base de datos de mariadb',
    version = '1', 
    contact = {
        "name": "Starlord",
        "url": "https://github.com/WolverinLando",
        "email":"orlandourbanotrejo@gmail.com"
    }, 
    debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)



def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"  
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response

@app.middleware("http")
async def add_custom_headers(request, call_next):
    response = await call_next(request)
    return add_cors_headers(response)

# Creates an event to establish the connection to the database before the server starts.
@app.on_event('startup')
def startup():
    if conexion.is_closed():
        conexion.connect()
        conexion.create_tables([Persona])
        print('Conexion exitosa')

# Creates an event to close the connection to the database before the server shuts down.
@app.on_event('shutdown')
def shutdown():
    if not conexion.is_closed():
        conexion.close()
        print('Apagando...');
        
app.include_router(persona)

# Allows multiple requests to be executed and resolved asynchronously. 
@app.get('/')
async def index():
    return 'Prueba de servidor exitosa'

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=5690)
