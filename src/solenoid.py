from abc import ABC, abstractmethod
from typing import Dict, Optional


class Solenoid(ABC):
    pin: int

    @abstractmethod
    def open(self):
        """
        opens solenoid
        :return: None
        """

    @abstractmethod
    def close(self):
        """
        closes solenoid
        :return: None
        """

    @abstractmethod
    def is_open(self) -> bool:
        """
        gets current state of this solenoid
        :return: SolenoidState
        """


_ingredient_solenoids: Dict[str, Solenoid] = dict()

def get_solenoid(ingredient: str) -> Optional[Solenoid]:
    """
    Gets the olenoid for the specified ingredient from the dict stored in this module.
    If no solenoid for that ingredient, returns None
    :param ingredient: ingredient requested
    :return: a Solenoid
    """
    if ingredient not in _ingredient_solenoids:
        return None

    return _ingredient_solenoids[ingredient]


def add_solenoid(solenoid: Solenoid, ingredient: str):
    """
    Adds given solenoid/ingredient pair to the dict, can be retreived later
    :param solenoid: Solenoid object. has to be init'd somewhere else
    :param ingredient: what ingredient it dispenses
    :return: None
    """
    _ingredient_solenoids[ingredient] = solenoid
