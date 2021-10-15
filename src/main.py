from typing import Dict

from solenoid import Solenoid
from pour import Pour

solenoids: Dict[str, Solenoid] = dict()


def make_pour(ingredient: str, amount: float) -> Pour:
    """
    Creates a Pour object of the subclass we're using
    :param ingredient:
    :param amount:
    :return: a Pour
    """
    # TODO implement