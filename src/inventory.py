from typing import List

from sensor import get_amount_sensor

installed_ingredients: List[str] = list()  # Keeps track of which ingredients are 'installed'
MIN_AMOUNT: float = 2  # the minimum amount of an ingredient needed to say it is available


def get_current_beverages() -> List[str]:
    """
    Gets the current beverages that are available
    :return: list of beverage names
    """
    return [ingredient for ingredient in installed_ingredients if get_amount(ingredient) > MIN_AMOUNT]


def get_amount(ingredient: str) -> float:
    """
    gets the current amount of given ingredient
    :param ingredient: the ingredient
    :return: float, sensor value
    """
    return get_amount_sensor(ingredient).get_value()
