import reflex as rx
from ..styles import styles


def frame(*args, **kwargs):
    return rx.vstack(
        rx.flex(
            *args,
            **kwargs,
            style=styles.FRAME
        )
    )