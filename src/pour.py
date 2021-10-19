"""
Contains Pour base class, Pour Factory base class, and
functions and data structures to manage active pours.
"""

from abc import ABC, abstractmethod
from typing import List

from src.solenoid import Solenoid


class Pour(ABC):
    solenoid: Solenoid
    recipe_amount: float
    current_amount: float

    @abstractmethod
    def __init__(self):
        self.current_amount = 0

    def start_pour(self):
        """
        Starts this pour
        :return: None
        """
        self.solenoid.open()

    def stop_pour(self):
        """
        Stops this pour
        :return:
        """
        self.solenoid.close()

    def is_pouring(self) -> bool:
        """
        Whether this pour is currently pouring
        :return: bool
        """
        return self.solenoid.is_open()

    def get_progress(self) -> float:
        """
        Gets this pour's progress as a percentage
        :return: float btwn 0 and 1
        """
        return self.current_amount / self.recipe_amount

    def update(self):
        """
        Needs to be called repeatedly and frequently. Checks this pour progress and stops it if it is done.
        :return: None
        """


pours_occurring: List[Pour] = list()


def add_pour(pour: Pour):
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
    @abstractmethod
    def make_pour(ingredient: str, amount: float) -> Pour:
        """
        Creates a Pour object of the subclass we're using
        :param ingredient: which ingredient
        :param amount:
        :return: a Pour
        """