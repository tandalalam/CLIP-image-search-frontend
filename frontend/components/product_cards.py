from states.query_state import QueryState, Product
import reflex as rx


def product(product_item: Product):
    image_link = product_item.image_link
    name = product_item.name
    price = product_item.price
    currency = product_item.currency
    link = product_item.link

    return rx.card(
        rx.inset(
            rx.image(src=image_link, ),
            side="top",
            pb="current",
        ),
        rx.link(
            rx.flex(
                rx.text(name, size="2", weight="bold"),
                rx.text(
                    f'{price} {currency}', size="1", color_scheme="gray"
                ),
                direction="row",
                spacing="1",
            ),
            href=link,
            is_external=True
        ),
        height="20vw"
    )


def in_chat_product(product_item: Product):
    image_link = product_item.image_link
    name = product_item.name
    price = product_item.price
    currency = product_item.currency
    link = product_item.link

    return rx.scroll_area(
        rx.card(
            rx.inset(
                rx.image(src=image_link, ),
                side="top",
                pb="current",
            ),
            rx.link(
                rx.flex(
                    rx.text(name, size="2", weight="bold"),
                    rx.text(
                        f'{price} {currency}', size="1", color_scheme="gray"
                    ),
                    direction="row",
                    spacing="1",
                ),
                href=link,
                is_external=True
            ),
            height="10vw",
            color_scheme="gray"
        )
    )


def product_grid():
    return rx.cond(QueryState.processing,
                   rx.spinner(size="10"),
                   rx.grid(
                       rx.foreach(
                           QueryState.results,
                           product,
                       ),
                       columns="3",
                       rows="aut",
                       flow="row",
                       justify="between",
                       spacing="8",
                       width="90%",
                       align="center",
                   )
                )


def product_grid_for_in_chat_response():
    return rx.cond(
        QueryState.processing,
        rx.icon(
            tag="loader-circle",
            size=19,
            color="white",
            class_name="animate-spin",
        ),
        rx.grid(
            rx.foreach(
                QueryState.results,
                in_chat_product,
            ),
            columns="5",
            rows="aut",
            flow="row",
            justify="center",
            spacing="3",
            width="100%",
            align="center",
        )
    )
