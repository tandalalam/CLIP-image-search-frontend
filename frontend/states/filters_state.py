import reflex as rx
from typing import List

from frontend.utils.api_controller import APIController
from frontend.states.models.filter import Filter, FilterType


class FilterState(rx.State):
    form_data: dict = {}
    filters: List[Filter] = [
        Filter(name="brand",
               possible_choices=['first', 'second'],
               type=FilterType(FilterType.MATCH))
    ]

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = {key: value for key, value in form_data.items() if value}

    @rx.event
    def get_filters(self, is_open):
        if is_open:
            api_controller = APIController.get_api_controller()
            self.filters = [
                Filter(**kwargs) for kwargs in api_controller.get_all_filters()
            ]
