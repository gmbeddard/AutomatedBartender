from typing import Dict, Type
from uuid import UUID

# from sensor import get_amount_sensor
# from solenoid import add_solenoid, get_solenoid
from src.pour import Pour_Factory, add_pour
from src.drink import Drink
from src.recipe import Recipe_Factory, JSON_Recipe_Factory

# implementation specific imports
from src.pseudo_implementations.timed_pour import Timed_Pour_Factory


# Factory declarations for specific implementation
pour_factory: Type[Pour_Factory] = Timed_Pour_Factory
recipe_parser: Type[Recipe_Factory] = JSON_Recipe_Factory
# TODO make real ones


finished_drinks: Dict[UUID, Drink] = dict()


def make_drink(drink: Drink):
    """
    takes every step of a drinks recipe and puts them on the pour queue
    :param drink: the drink to make
    :return: None
    """
    for pour in drink.get_pours():
        add_pour(pour)

