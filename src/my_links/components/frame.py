import reflex as rx
from ..styles import styles


def frame(*args, **kwargs):
    return rx.chakra.vstack(
        rx.chakra.flex(
            *args,
            **kwargs,
            style=styles.FRAME
        )
    )