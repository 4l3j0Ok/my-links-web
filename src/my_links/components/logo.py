import reflex as rx
from ..modules.config import App
from ..styles.sizes import Size
from ..styles import styles


def logo(with_link = True, **kwargs) -> rx.Component:
    return rx.chakra.link(
            rx.chakra.image(
            src="./logo.svg",
            href=App.url.value,
            is_external=True,
            **kwargs,
        )
    ) if with_link else rx.chakra.image(
            src="./logo.svg",
            **kwargs,
        )
