from typing import Dict
from requests import request
from utils.configs.configs import ConfigManager


class APIController:
    api_controller = None

    @staticmethod
    def get_api_controller():
        if APIController.api_controller is None:
            APIController.api_controller = APIController()
        return APIController.api_controller

    def __init__(self):
        self.backend_url = ConfigManager.get_config_manager().get_prop('backend_configs').get('backend_url')

    def search(self, term, filters: Dict = None):
        if filters is None:
            filters = {}

        url = self.backend_url + '/search'

        payload = ""
        headers = {
            'Content-Type': 'application/json'
        }

        response = request("GET",
                           url,
                           params=dict(query=term,
                                       **filters),
                           headers=headers,
                           data=payload)

        if response.status_code == 200:
            data = response.json()
        else:
            data = []

        return data

    def get_all_filters(self):
        sample_response = [
            {
                'name': 'currency',
                'possible_choices': ['QAR', 'KWD', 'OMR', 'AED', 'SAR', 'BHD', 'USD'],
                'type': 'option'
            },
            {
                'name': 'brand',
                'possible_choices': ['boohoo', 'Trendyol', 'Beverly Hills Polo Club', 'Nine West', 'Aldo', 'Herschel',
                                     'Crocs', 'Tommy Hilfiger', 'Koton', 'Puma', 'Clarks', 'Dune London',
                                     'Michael Kors',
                                     'Tommy Jeans', 'Jack & Jones', 'Aeropostale', 'FitFlop', 'Jimmy Choo', 'Adidas',
                                     'Burton', 'Havaianas', 'Polo Ralph Lauren', 'Under Armour', 'Skechers',
                                     'Steve Madden', 'Nasty Gal', 'Birkenstock', "Levi's", 'Toms', 'Lacoste',
                                     'Calvin Klein Jeans', 'Hummel', 'Vero Moda', 'Hush Puppies', 'Calvin Klein',
                                     'Naturalizer', 'Adidas Originals', 'Easy Spirit', 'American Eagle', "Marc O'Polo",
                                     'Only', 'Casio', 'DeFacto', 'Vans', 'Nike', 'U.S. Polo Assn.', 'Bzees',
                                     'Armani Exchange', 'Little Mistress', 'Ted Baker', 'Asics', 'Revolution', 'Fila',
                                     'Geox', 'Timberland', 'Elie Saab', 'Vionic', 'Closet London', 'Sprayground',
                                     'Camper', 'DSQUARED2', 'Chopard', 'KENDALL + KYLIE', 'Diesel', 'Carolina Herrera',
                                     'The North Face', 'Nautica', 'Love Moschino', 'Teva', 'Bebe', 'Carrera',
                                     'Valentino', 'Camelbak', 'Anne Klein', 'Abercrombie & Fitch', 'Kate Spade',
                                     'Reebok', 'Ralph Lauren', 'New Balance', 'Marc Jacobs', 'Hermes', 'Givenchy',
                                     'Converse'],
                'type': 'option'
            },
            {
                'name': 'category_name',
                'possible_choices': ['tops', 'shirts', 'sweatshirts', 'bags', 'watches', 'shoes', 'earrings',
                                     'keychains', 'belts', 'headbands', 'dresses', 't-shirts', 'raincoats',
                                     'sunglasses',
                                     'kimonos', 'blouses', 'shorts', 'hoodies', 'waistcoats', 'scarves', 'anklets',
                                     'scrunchies', 'rings', 'pants', 'skirts', 'jackets', 'sweaters', 'bracelets',
                                     'necklaces', 'socks', 'blazers', 'coats', 'ties', 'hats', 'bodysuits', 'jalabiyas',
                                     'jumpsuits', 'turbans', 'bras', 'swimwears', 'slippers', 'briefs', 'abayas',
                                     'shackets', 'suits', 'cases', 'patches', 'gloves', 'capes', 'polo shirts',
                                     'kaftans', 'jewelry sets'],
                'type': 'option'

            }

        ]

        return sample_response
