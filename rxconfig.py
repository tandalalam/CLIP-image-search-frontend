import reflex as rx
from frontend.style import create_colors_dict

config = rx.Config(
    app_name="frontend",
    api_url="http://0.0.0.0:8000",
    tailwind={
        "darkMode": "class",
        "theme": {
            "colors": {
                **create_colors_dict(),
            },
        },
    },
)
