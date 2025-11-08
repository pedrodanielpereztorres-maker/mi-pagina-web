import reflex as rx
import sqlmodel
from sqlmodel import Session, create_engine, SQLModel, Field
from os import environ

# Configuración de la base de datos
# Usar una variable de entorno para la URL de la base de datos es crucial en producción.
DATABASE_URL = environ.get("DATABASE_URL", "postgresql://user:password@host:port/database")
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@rx.ModelRegistry.register
class Usuarios(SQLModel, table=True):
    id_usuario: int | None = Field(default=None, primary_key=True)
    nombre: str
    correo: str
    mensaje: str

def save_usuario(nombre: str, correo: str, mensaje: str):
    with Session(engine) as session:
        new_usuario = Usuarios(nombre=nombre, correo=correo, mensaje=mensaje)
        session.add(new_usuario)
        session.commit()
        session.refresh(new_usuario)
    return new_usuario
