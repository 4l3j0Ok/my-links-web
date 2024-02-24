import reflex as rx
from ..styles import styles
from ..components.button import button
from ..components.frame import frame
from ..modules import config
from ..styles.sizes import Size


def links() -> rx.Component:
    highlight = config.Highlight.links.value
    professional = config.Professional.links.value
    social = config.Social.links.value
    return frame(
        # Highlight
        rx.chakra.heading("Destacados"),
        *[button(
            title=item.get("title"),
            description=item.get("description"),
            icon=item.get("icon"),
            href=item.get("href")
        ) for item in highlight.values()],
        # Professional
        rx.chakra.heading("Profesional"),
        *[button(
            title=item.get("title"),
            description=item.get("description"),
            icon=item.get("icon"),
            href=item.get("href")
        ) for item in professional.values()],
        # Social
        rx.chakra.heading("Social"),
        *[button(
            title=item.get("title"),
            description=item.get("description"),
            icon=item.get("icon"),
            href=item.get("href")
        ) for item in social.values()],
    )
