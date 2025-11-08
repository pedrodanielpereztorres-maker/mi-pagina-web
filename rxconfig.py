import reflex as rx
import os

config = rx.Config(
    app_name="hola",
    db_url=os.environ.get("DATABASE_URL"),
    api_url="https://mi-pagina-web-y37z.onrender.com/api",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
