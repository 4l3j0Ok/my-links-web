import reflex as rx
from .react.icons import iconify
from ..styles.sizes import Size


def button(title: str = "", description: str = "", icon: str = "", href: str = "#", **args) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.hstack(
            iconify(
                icon,
                font_size=Size.xlarge.value,
                padding_x=Size.xsmall.value,
            ),
            rx.chakra.vstack(
                rx.chakra.text(title, as_="b"),
                rx.chakra.text(
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