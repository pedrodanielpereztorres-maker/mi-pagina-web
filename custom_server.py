from fastapi import FastAPI, Request
from backend_api import save_usuario, create_db_and_tables
from pydantic import BaseModel
import reflex as rx
from hola.hola import create_reflex_app # Importar la función para crear la app Reflex
from starlette.staticfiles import StaticFiles
import os

# Define un modelo Pydantic para los datos del formulario
class ContactForm(BaseModel):
    nombre: str
    correo: str
    mensaje: str

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/contact")
async def contact_submit(form_data: ContactForm):
    try:
        save_usuario(form_data.nombre, form_data.correo, form_data.mensaje)
        return {"message": "Formulario enviado con éxito"}
    except Exception as e:
        return {"message": f"Error al guardar el formulario: {str(e)}", "status": "error"}

# Inicializar la aplicación Reflex y montarla en la aplicación FastAPI
rx_app = create_reflex_app(api_transformer=app)

# Montar los archivos estáticos de Reflex
current_dir = os.path.dirname(os.path.abspath(__file__))
static_files_path = os.path.join(current_dir, ".web", "_static")
app.mount("/_static", StaticFiles(directory=static_files_path), name="static")

# Montar la aplicación Reflex en la raíz
app.mount("/", rx_app)