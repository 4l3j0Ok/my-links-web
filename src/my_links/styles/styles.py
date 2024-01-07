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
    "font-family": Font.DEFAULT.value,
    "font-size": Size.small.value,
    "::selection": {
        "background": Palette.pink.value,
        "color": Palette.white.value,
    },
    "::moz-selection": {
        "background": Palette.pink.value,
        "color": Palette.white.value,
    },
    ".button": {
        "display": "inline-block",
        "overflow": "hidden",
        "white-space": "wrap",
        "text-align": "start",
        "width": "100%",
        "height": "auto",
        "font-size": Size.medium.value,
        "margin-y": Size.small.value,
        "padding": Size.normal.value,
        "background": f"{Palette.light_gray.value}",
        ":hover": {
            "background": f"{Palette.xlight_gray.value}"
        },
        "transition": ".3s ease-in-out",
        "border-radius": Size.medium.value,
    },
    rx.Heading: {
        "font-family": Font.DEFAULT.value,
        "font-size": Size.xlarge.value,
        "margin-y": Size.small.value,
        "width": "100%",
    },
    rx.Image: {
        "pointer-events": "none",
        "user-select": "none",
    },
    rx.Link: {
        ":hover": {
            "text-decoration": "none",
        }
    },
}


FRAME = {
    "width": "100%",
    "max-width": "600px",
    "align-items": "center",
    "background": Palette.dark_gray.value,
    "border-radius": Size.normal.value,
    "flex-direction": "column",
    "padding": Size.xxlarge.value,
    "margin-top": Size.xlarge.value,
}
