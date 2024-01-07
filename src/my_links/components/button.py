import reflex as rx
from .react.icons import iconify
from ..styles.sizes import Size


def button(title: str = "", description: str = "", icon: str = "", href: str = "#", **args) -> rx.Component:
    return rx.link(
        rx.hstack(
            iconify(
                icon,
                font_size=Size.xlarge.value,
                padding_x=Size.xsmall.value,
            ),
            rx.vstack(
                rx.text(title, as_="b"),
                rx.text(
                    description,
                    font_size=Size.small.value,
                ),
                align_items="flex-start",
            ),
        ),
        class_name="button",
        href=href,
        is_external=True,
        width="100%",
        **args
    )