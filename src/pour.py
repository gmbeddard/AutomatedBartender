from abc import ABC, abstractmethod

from solenoid import Solenoid

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