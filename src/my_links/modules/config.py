from enum import Enum


class StyleSheet(Enum):
    google_fonts = "https://fonts.googleapis.com/css?family={font_name}&display=swap"


class Highlight(Enum):
    links = {
        "alejoide": {
            "title": "Alejoide",
            "description": "Mi sitio web personal.",
            "icon": "dashicons:star-filled",
            "href": "https://alejoide.com"
        }
    }


class Professional(Enum):
    links = {
        "github": {
            "title": "Github",
            "description": "Todos mis proyectos personales de código abierto.",
            "icon": "fa-brands:github",
            "href": "https://github.com/4l3j0Ok"
        },
        "linkedin": {
            "title": "Linkedin",
            "description": "Mi perfil profesional y red de contactos.",
            "icon": "fa-brands:linkedin",
            "href": "https://linkedin.com/in/alejoide"
        },
        "email": {
            "title": "Email",
            "description": "Contáctame por correo electrónico: contacto@alejoide.com.",
            "icon": "fa-solid:envelope",
            "href": "mailto:contacto@alejoide.com"
        }
    }


class Social(Enum):
    links = {
        "instagram": {
            "title": "Instagram",
            "description": "Sígueme en Instagram.",
            "icon": "ri:instagram-fill",
            "href": "https://instagram.com/4l3j0"
        },
        "twitter": {
            "title": "Twitter",
            "description": "Conéctate conmigo en Twitter.",
            "icon": "fa-brands:twitter",
            "href": "https://twitter.com/alejoide_"
        },
        "youtube": {
            "title": "Youtube | General",
            "description": "Suscríbete a mi canal de Youtube donde subo edits y contenido variado.",
            "icon": "fa-brands:youtube",
            "href": "https://www.youtube.com/@alejo_okay"
        },
        "youtube_gaming": {
            "title": "Youtube | Juegos",
            "description": "Suscríbete a mi canal de Youtube de juegos.",
            "icon": "fa-brands:youtube",
            "href": "http://www.youtube.com/@AlejoideFG"
        }
    }
