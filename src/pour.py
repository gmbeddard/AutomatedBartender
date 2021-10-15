from abc import ABC

from solenoid import Solenoid

class Pour(ABC):
    solenoid: Solenoid
    recipe_amount: float
    current_amount: float

    def start_pour(self):
        """
        Starts this pour
        :return: None
        """

    def stop_pour(self):
        """
        Stops this pour
        :return:
        """

    def get_progress(self) -> float:
        """
        Gets this pour's progress as a percentage
        :return: float btwn 0 and 1
        """

    def update(self):
        """
        Needs to be called repeatedly and frequently. Checks this pour progress and stops it if it is done.
        :return: None
        """