import fastapi
from fastapi.staticfiles import StaticFiles
import reflex as rx

# Importar la app de Reflex desde tu proyecto
from hola.hola import app as reflex_app

# Compilar la app de Reflex para asegurar que los archivos del frontend se generen
reflex_app.compile()

# Crear una nueva aplicación FastAPI
app = fastapi.FastAPI()

# Montar el backend de Reflex (API y WebSocket) en la ruta /api
# El objeto reflex_app.api es una aplicación FastAPI que contiene todas las rutas del backend.
app.mount(path="/api", app=reflex_app.api)

# Montar los archivos estáticos del frontend
# Esto servirá el index.html y todos los assets (JS, CSS) desde la raíz.
app.mount(path="/", app=StaticFiles(directory=".web", html=True), name="static")
