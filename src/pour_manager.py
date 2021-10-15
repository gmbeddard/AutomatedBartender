from abc import ABC
from typing import List

from pour import Pour
from timed_pour import Timed_Pour
from main import ingredient_solenoids

pours_occurring: List[Pour] = list()


def add_pour(pour):
    """
    Adds pour to the list
    :param pour: obj to add to queue
    :return: None
    """
    pours_occurring.append(pour)
    pour.start_pour()


def update_pours():
    """
    Updates all pours that are active. removes finished pours
    :return: None
    """
    for pour in pours_occurring:
        pour.update()
        if pour.get_progress() >= 1.0:
            pours_occurring.remove(pour)


class Pour_Factory(ABC):
    @staticmethod
    def make_pour(ingredient: str, amount: float):
        """
        Creates a Pour object of the subclass we're using
        :param ingredient: which ingredient
        :param amount:
        :return: a Pour
        """


class Timed_Pour_Factory(Pour_Factory):
    """
    Implementation of above ABC. this one makes timed pours which are kind of useless for the real project
    """
    @staticmethod
    def make_pour(ingredient: str, amount: float):
        pour = Timed_Pour
        pour.solenoid = ingredient_solenoids[ingredient]
        pour.recipe_amount = amount
        add_pour(pour)
        return pour