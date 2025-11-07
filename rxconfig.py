import reflex as rx
import os

config = rx.Config(
    app_name="hola",
    db_url=os.environ.get("DATABASE_URL", "postgresql://postgres:V32273930@localhost:5432/mi_pagina"),
    api_url=os.environ.get("RENDER_EXTERNAL_URL"),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
