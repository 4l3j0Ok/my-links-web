import reflex as rx
from .views.header import header
from .views.links import links
from .views.footer import footer
from .styles import styles
from .modules.config import GoogleAnalytics


@rx.page(route="/", title="Alejoide | Mis Links", description="Todos mis links en un solo lugar.")
def index() -> rx.Component:
    return rx.box(
        header(),
        links(),
        footer(),
    )


app = rx.App(
    style=styles.BASE,
    stylesheets=styles.STYLESHEETS,
    head_components=[
        rx.script(src=GoogleAnalytics.INIT_SCRIPT_URL.value),
        rx.script(GoogleAnalytics.SEND_DATA_SCRIPT.value),
    ]
)
