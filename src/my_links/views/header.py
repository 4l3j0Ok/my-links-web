import reflex as rx
from ..styles.sizes import Size
from ..components.images import profile
from ..components.frame import frame


def header() -> rx.Component:
    return frame(
        rx.hstack(
            profile(
                "./me.jpeg",
                alt_text="Alejo Sarmiento",
                width=Size.xxxxlarge.value,
                margin_right=Size.xlarge.value,
                display="block",
                flex_shrink= 0
            ),
            rx.vstack(
                rx.heading("Alejo Sarmiento", margin_y=".2em"),
                rx.text(
                    "SRE y desarrollador de software.",
                    flex_wrap="wrap",
                ),
                align_items="flex-start",
            ),
            align_items="center",
            width="100%",
        ),
    )