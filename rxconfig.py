import reflex as rx
import os

config = rx.Config(
    app_name="hola",
    db_url=os.environ.get("DATABASE_URL"),
    api_url=f"{os.environ.get('RENDER_EXTERNAL_URL', '').replace('https://', 'wss://')}:8000/_event",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
