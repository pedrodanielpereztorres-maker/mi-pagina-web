import reflex as rx

config = rx.Config(
    app_name="hola",
    db_url="postgresql://postgres:V32273930@localhost:5432/mi_pagina",
    api_url="https://YOUR_BACKEND_URL:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]

)
