from typing import List, Optional

import strawberry

from strawberry_garden.garden.type import Garden
from strawberry_garden.fruit.type import Fruit

GARDEN_LIST = [
    Garden(name='Harmony Park', fruits=[
        Fruit(name='strawberry', color='red', quantity=10),
        Fruit(name='blueberry', color='blue', quantity=20),
        Fruit(name='kiwi', color='green', quantity=6),
    ]),
    Garden(name='Paradise Place', fruits=[
        Fruit(name='pineapple', color='yellow', quantity=3),
        Fruit(name='raspberry', color='red', quantity=23),
    ]),
]


@strawberry.type
class GardenQueries:
    """ Query definitions for Garden objects. """

    @strawberry.field
    def gardens(self) -> List[Garden]:
        """ Query to return all Garden objects. """
        return GARDEN_LIST

    @strawberry.field
    def garden(self, name: str) -> Optional[Garden]:
        """ Query to return Garden object based on name. """
        found_value = next(iter(list(filter(lambda x: x.name == name, GARDEN_LIST))), None)
        return found_value
