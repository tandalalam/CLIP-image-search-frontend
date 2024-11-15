import reflex as rx
from frontend import style
from states.chat_state import SettingsState
from frontend.components.chat import chat, action_bar


def chat_index() -> rx.Component:
    return rx.theme(
        rx.el.style(
            f"""
            :root {{
                --font-family: "{SettingsState.font_family}", sans-serif;
            }}
        """
        ),
        rx.box(
            chat(),
            action_bar(),
            class_name="relative flex flex-col justify-between gap-20 mx-auto px-6 pt-16 lg:pt-6 pb-6 max-w-4xl h-screen",
        ),
    )


app = rx.App(stylesheets=style.STYLESHEETS, style={"font_family": "var(--font-family)"})
