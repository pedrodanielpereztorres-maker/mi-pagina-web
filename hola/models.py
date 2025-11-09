import reflex as rx
import sqlmodel
from typing import Optional

class Usuarios(rx.Model, table=True, extend_existing=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    correo: str
    mensaje: str
