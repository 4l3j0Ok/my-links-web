import reflex as rx
from .react.icons import iconify
from ..styles.sizes import Size


def button(title: str = "", description: str = "", icon: str = "", href: str = "#", **args) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                iconify(
                    icon,
                    font_size=Size.xlarge.value,
                    padding_x=Size.xsmall.value
                ),
                rx.vstack(
                    rx.span(title),
                    rx.span(
                        description,
                        font_size=Size.small.value,
                    ),
                    align_items="flex-start",
                ),
            ),
            **args
        ),
        href=href,
        is_external=True,
        width="100%",
    )