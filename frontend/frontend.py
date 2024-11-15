import reflex as rx

from frontend.chat_page import chat_index
from states.query_state import QueryState
from frontend.components.filters import filter_menu
from frontend.components.product_cards import product_grid


def search_bar():
    return rx.box(
        rx.input(
            rx.input.slot(
                rx.hstack(
                    filter_menu(),
                    rx.icon("search",
                            on_click=QueryState.search('enter'))
                )
            ),
            color_scheme="blue",
            class_name="rounded-full w-full outline-none focus:outline-accent-10 h-[48px] text-slate-12 placeholder:text-slate-9",
            placeholder="Search here...",
            value=QueryState.text,
            on_change=QueryState.set_text,
            on_key_down=QueryState.search,
        ),
        class_name="relative w-full rounded-full",
    )


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.box(
                rx.heading("Find your style!",
                           size="9",
                           align="center"),
                width='100%'),
            search_bar(),
            product_grid(),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
        ),
        rx.box(
            rx.link(rx.hstack(
                rx.text('Ask AI', size="2", align="center"),
                rx.button(rx.image('/chatbot.svg')),
                align="center",
                justify="center"
            ),
                href='/chat',
                is_external=False
            ),
            padding='10px')
    )


app = rx.App()
app.add_page(index)
app.add_page(chat_index, route='/chat')
