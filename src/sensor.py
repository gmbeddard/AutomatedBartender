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


class Always_1_Sensor(Sensor):
    def get_value(self) -> float:
        return 1.0


_ingredient_amount_sensors: Dict[str, Sensor] = dict()
_ingredient_temperature_sensors: Dict[str, Sensor] = dict()
_ready_to_pour_sensor: Optional[Sensor] = None


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


def get_temp_sensor(ingredient: str) -> Optional[Sensor]:
    """
    Gets the temperature sensor for the specified ingredient from the dict stored in this module.
    If no sensor for that ingredient, returns None
    :param ingredient: ingredient requested
    :return: a Sensor
    """
    if ingredient not in _ingredient_temperature_sensors:
        return None

    return _ingredient_temperature_sensors[ingredient]

def add_temperature_sensor(sensor: Sensor, ingredient: str):
    """
    Adds given sensor/ingredient pair to the dict, can be retreived later
    :param sensor: Sensor object. has to be init'd somewhere else
    :param ingredient: what ingredient it measures
    :return: None
    """
    _ingredient_temperature_sensors[ingredient] = sensor


def set_pour_ready_sensor(sensor: Sensor):
    """
    Sets the sensor that detects if a glass is present (ready to pour)
    :param sensor: sensor
    :return: None
    """
    global _ready_to_pour_sensor
    _ready_to_pour_sensor = sensor

def ready_to_pour() -> bool:
    """
    reads internal ready_to_pour sensor, determines if safe.
    :return: true if yes
    """

    if _ready_to_pour_sensor is None:
        return False

    # TODO depends on how the sensor works. implement when thts implemented
    if _ready_to_pour_sensor.get_value() >= 1.0:
        return True

    return False