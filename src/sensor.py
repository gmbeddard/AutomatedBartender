from abc import ABC, abstractmethod
from typing import Dict, Optional


# TODO fill out. Idrk what sensors need to do at this point
class Sensor(ABC):
    pin: int

    @abstractmethod
    def get_value(self) -> float:
        """
        gets value from the sensor
        :return: None
        """


_ingredient_amount_sensors: Dict[str, Sensor] = dict()

def get_amount_sensor(ingredient: str) -> Optional[Sensor]:
    """
    Gets the amount sensor for the specified ingredient from the dict stored in this module.
    If no sensor for that ingredient, returns None
    :param ingredient: ingredient requested
    :return: a Sensor
    """
    if ingredient not in _ingredient_amount_sensors:
        return None

    return _ingredient_amount_sensors[ingredient]


def add_amount_sensor(sensor: Sensor, ingredient: str):
    """
    Adds given sensor/ingredient pair to the dict, can be retreived later
    :param sensor: Sensor object. has to be init'd somewhere else
    :param ingredient: what ingredient it measures
    :return: None
    """
    _ingredient_amount_sensors[ingredient] = sensor
