import reflex as rx
from .views.header import header
from .views.links import links
from .styles import styles



@rx.page(route="/", title="Mis links", description="")
def index() -> rx.Component:
    return rx.box(
        header(),
        links(),
    )


app = rx.App(style=styles.BASE)
app.compile()
