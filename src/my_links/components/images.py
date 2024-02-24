import reflex as rx
from ..styles.sizes import Size
from ..styles import colors


def profile(
        asset: str,
        alt_text: str = "",
        border_size: Size = Size.xsmall.value,
        border_color: colors = colors.Palette.light_gray.value,
        **args
    ) -> rx.Component:
    return rx.chakra.image(
        src=asset,
        alt=alt_text,
        border_radius="50%",
        overflow="hidden",
        border=f"{border_size} solid {border_color}",
        object_fit="cover",
        **args
    )