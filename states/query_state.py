import reflex as rx
from states.filters_state import FilterState
from utils.api_controller import APIController
from states.models.product import Product


class QueryState(rx.State):
    text: str
    results: list[Product] = []
    processing: bool = False

    @rx.event
    def get_search_event(self, key):
        return self.search(key)

    @rx.event
    async def search(self, key):
        filter_state = await self.get_state(FilterState)

        if key.lower() == 'enter':
            self.processing = True
            yield

            api_controller = APIController.get_api_controller()
            data = api_controller.search(term=self.text, filters=filter_state.form_data)

            self.results = [Product(
                link=product['link'],
                image_link=product['images'][0],
                price=product['price'],
                name=product['name'],
                currency=product['currency']
            ) for product in data]

            self.processing = False
