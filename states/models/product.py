import reflex as rx


class Product(rx.Base):
    link: str
    image_link: str
    price: float
    currency: str
    name: str
