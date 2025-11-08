
import reflex as rx
from hola.hola import app as reflex_app
from fastapi import FastAPI

# This gets the underlying FastAPI app that serves both the backend and the frontend.
app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

app.mount("/", reflex_app.api)
