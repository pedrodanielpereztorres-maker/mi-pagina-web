from fastapi import FastAPI, Request
from backend_api import save_usuario, create_db_and_tables
from pydantic import BaseModel

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