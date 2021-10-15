from typing import Dict
from uuid import UUID

from solenoid import Solenoid
from sensor import Sensor
from pour_manager import Timed_Pour_Factory, add_pour
from src.drink import Drink

ingredient_solenoids: Dict[str, Solenoid] = dict()
ingredient_amount_sensors: Dict[str, Sensor] = dict()
#TODO fill in these solenoids somewhere

pour_factory = Timed_Pour_Factory  # Indicates which type of pour factory is being used
# TODO make a better type of pour + factory that actually uses the sensors and replace this with it

finished_drinks: Dict[UUID, Drink] = dict()


def make_drink(drink: Drink):
    """
    takes every step of a drinks recipe and puts them on the pour queue
    :param drink: the drink to make
    :return: None
    """
    for pour in drink.get_pours():
        add_pour(pour)

