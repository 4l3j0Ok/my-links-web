from datetime import date
import reflex as rx
from ..components.frame import frame
from ..modules.config import App
from ..styles.sizes import Size
from ..components.logo import logo


def footer() -> rx.Component:
    return frame(
        logo(
            with_link=False,
            width=Size.xxxxxlarge.value,
            height="auto",
            margin_bottom=Size.large.value,
        ),
        rx.text(
            f"© 2023 - {date.today().year}" if date.today().year > 2023 else f"© 2023",
            rx.span(" "),
            rx.link(
                f"{App.name.value} by {App.author.value}",
                href=App.url.value,
            ),
            rx.span(" "),
            App.version.value,
            rx.span("."),
        ),
        margin_bottom=Size.large.value,
    )