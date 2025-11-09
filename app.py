import reflex as rx
from hola.hola import pagina_principal

# Crea la instancia de la app de Reflex.
app = rx.App(
    stylesheets=["/custom.css"],
)
app.add_page(pagina_principal, route="/")