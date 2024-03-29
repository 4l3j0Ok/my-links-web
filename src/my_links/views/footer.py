from datetime import date
import reflex as rx
from ..components.frame import frame
from ..modules.config import App
from ..styles.sizes import Size
from ..components.logo import logo
from ..styles.colors import Palette


def footer() -> rx.Component:
    return frame(
        logo(
            with_link=False,
            width=Size.xxxxxlarge.value,
            height="auto",
            margin_bottom=Size.large.value,
        ),
        rx.chakra.text(
            f"© 2023 - {date.today().year}" if date.today().year > 2023 else f"© 2023",
            rx.chakra.span(" "),
            rx.chakra.link(
                f"{App.name.value} by {App.author.value}",
                href=App.url.value,
                color=Palette.cyan.value,
                _hover={
                    "color": Palette.pink.value,
                },
                is_external=False,
            ),
            rx.chakra.span(" "),
            App.version.value,
            rx.chakra.span("."),
        ),
        margin_bottom=Size.large.value,
    )