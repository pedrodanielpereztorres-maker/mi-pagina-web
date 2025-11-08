import reflex as rx
import os

config = rx.Config(
    app_name="hola",
    db_url=os.environ.get("DATABASE_URL"),
    api_url="httpshttps://mi-pagina-web-y37z.onrender.com",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
