
import reflex as rx
from hola.hola import app as reflex_app

# This gets the underlying FastAPI app that serves both the backend and the frontend.
app = reflex_app.api
