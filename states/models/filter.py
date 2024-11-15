import reflex as rx
from enum import Enum
from typing import List


class FilterType(Enum):
    MATCH = 'option'
    RANGE = 'range'


class Filter(rx.Base):
    possible_choices: List[str]
    name: str
    type: FilterType = FilterType.MATCH

