import reflex as rx
from .colors import Palette
from .sizes import Size
from .fonts import Font
from ..modules.config import StyleSheet


STYLESHEETS = [
    StyleSheet.google_fonts.value.format(font_name=Font.DEFAULT.value),
]

BASE = {
    "background": Palette.black.value,
    "color": f"{Palette.white.value}",
    "font_family": Font.DEFAULT.value,
    "font_size": Size.small.value,
    rx.Heading: {
        "font_family": Font.DEFAULT.value,
        "font_size": Size.xlarge.value,
        "margin_y": Size.small.value,
        "width": "100%",
    },
    rx.Button: {
        "display": "inline-block",
        "overflow": "hidden",
        "white-space": "wrap",
        "text-align": "start",
        "width": "100%",
        "height": "auto",
        "margin_y": Size.small.value,
        "padding": Size.medium.value,
        "background": f"{Palette.light_gray.value}",
        ":hover": {
            "background": f"{Palette.xlight_gray.value}"
        },
        "transition": ".3s ease-in-out",
        "border-radius": Size.medium.value,
    },
}


FRAME = {
    "width": "100%",
    "max-width": "600px",
    "align-items": "center",
    "background": Palette.dark_gray.value,
    "border-radius": Size.medium.value,
    "flex-direction": "column",
    "padding": Size.xxlarge.value,
    "margin_top": Size.xlarge.value,
}
