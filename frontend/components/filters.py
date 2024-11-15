import reflex as rx
from frontend.states.filters_state import Filter, FilterType, FilterState


def get_filter(filter_obj: Filter):
    filter_type, possible_choices, name = filter_obj.type, filter_obj.possible_choices, filter_obj.name
    return rx.cond(filter_type == FilterType.MATCH,
                   rx.flex(
                       rx.text(name),
                       rx.divider(orientation="vertical", size="2"),
                       rx.select(
                           possible_choices,
                           name=name,
                           placeholder="Any"
                       ),
                       spacing='4',
                       align='center',
                       direction='row'
                   ),
                   rx.box()
                   )


def form_example():
    return rx.box(
        rx.form(
            rx.vstack(
                rx.foreach(
                    FilterState.filters,
                    get_filter
                ),
                rx.button("Submit Filters", type="submit"),
            ),
            on_submit=FilterState.handle_submit,
            reset_on_submit=False,
        ),
    )


def filter_menu():
    return rx.menu.root(
        rx.menu.trigger(
            rx.icon("filter", variant="soft"),
        ),
        rx.menu.content(
            form_example()
        ),
        on_open_change=FilterState.get_filters
    )
