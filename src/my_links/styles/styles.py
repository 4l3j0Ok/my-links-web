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
    "::selection": {
        "background": Palette.pink.value,
        "color": Palette.white.value,
    },
    "::moz_selection": {
        "background": Palette.pink.value,
        "color": Palette.white.value,
    },
    ".button": {
        "display": "inline_block",
        "overflow": "hidden",
        "white_space": "wrap",
        "text_align": "start",
        "width": "100%",
        "height": "auto",
        "font_size": Size.medium.value,
        "margin_y": Size.small.value,
        "padding": Size.normal.value,
        "background": f"{Palette.light_gray.value}",
        ":hover": {
            "background": f"{Palette.xlight_gray.value}"
        },
        "transition": ".3s ease_in_out",
        "border_radius": Size.medium.value,
    },
    rx.Heading: {
        "font_family": Font.DEFAULT.value,
        "font_size": Size.xlarge.value,
        "margin_y": Size.small.value,
        "width": "100%",
    },
    rx.Image: {
        "pointer_events": "none",
        "user_select": "none",
    },
    rx.Link: {
        ":hover": {
            "text_decoration": "none",
        }
    },
}


FRAME = {
    "width": "100%",
    "max_width": "600px",
    "align_items": "center",
    "background": Palette.dark_gray.value,
    "border_radius": Size.normal.value,
    "flex_direction": "column",
    "padding": Size.xxlarge.value,
    "margin_top": Size.xlarge.value,
}
