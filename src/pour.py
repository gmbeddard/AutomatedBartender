"""
Contains Pour base class, Pour Factory base class, and
functions and data structures to manage active pours.
"""

from abc import ABC, abstractmethod
from typing import List, Type
from time import perf_counter

from src.solenoid import Solenoid, get_solenoid


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

_TIMED_POUR_RATE = 0.8
class Timed_Pour(Pour):
    """
    Pour for time. uses no sensors. uses final float POUR_RATE to determine amount/time

    This is a 'default' implementation I am designing, probably wont be used.
    """

    start_tm: float

    def __init__(self):
        super().__init__()

    def start_pour(self):
        super()  # Opens solenoid
        self.start_tm = perf_counter()

    def update(self):
        if not self.is_pouring():
            return

        self.current_amount = (perf_counter() - self.start_tm) * _TIMED_POUR_RATE
        if self.current_amount >= self.recipe_amount:
            self.stop_pour()


# Keep track of pours that are currently active (maybe pouring, maybe queued to start)
_pours: List[Pour] = list()

def add_pour(pour: Pour):
    """
    adds pour to the list
    :param pour: pour obj
    :return: None
    """
    _pours.append(pour)

def start_all_pours():
    """
    Called when its time to make the next drink.
    moves all waiting pours from
    :return:
    """
    # TODO idk if we want all the pours to start at the same time or not lol
    for pour in _pours:
        pour.start_pour()

def update_all_pours():
    """
    Updates all pours that are active. removes finished pours
    :return: None
    """
    for pour in _pours:
        pour.update()
        if pour.get_progress() >= 1.0:
            _pours.remove(pour)

def waiting_for_pours() -> bool:
    """
    checks if pour manager is ready to be given more pours to handle for another drink
    :return:
    """
    return len(_pours) == 0


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

class Timed_Pour_Factory(Pour_Factory):
    """
    Implementation of above ABC. this one makes timed pours which are kind of useless for the real project
    """
    @staticmethod
    def make_pour(ingredient, amount):
        pour = Timed_Pour()
        pour.solenoid = get_solenoid(ingredient)
        pour.recipe_amount = amount
        return pour


# Set which pour factory we are going to use.
pour_factory: Type[Pour_Factory] = Timed_Pour_Factory