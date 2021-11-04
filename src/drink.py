from uuid import UUID, uuid4
from typing import List, Optional, Union

from src.recipe import Recipe, recipe_parser
from src.pour import Pour
from src.pour import pour_factory, add_pour


class Drink:
    recipe: Recipe
    ID: UUID
    _pours: Optional[List[Pour]]


    def __init__(self, recipe: Union[str, Recipe]):
        """
        :param recipe: recipe object, or str that has not been parsed yet
        """
        if isinstance(recipe, Recipe):
            self.recipe = recipe
        else:
            self.recipe = recipe_parser.parse_recipe_str(recipe)

        self.ID = uuid4()
        self._pours = None


    def _make_pours(self):
        """
        initializes pour list
        :return: None
        """
        self._pours = list()
        for ingredient in self.recipe:
            self._pours.append(pour_factory.make_pour(ingredient, self.recipe[ingredient]))


    def get_pours(self) -> List[Pour]:
        """
        Get a list of pours needed to make this drink.
        :return: list of pours
        """
        if self._pours is None:
            self._make_pours()
        return self._pours


    def get_progress(self) -> float:
        """
        Get's this drink's current progress: sum amount poured / total to pour
        :return: float btwn 0 and 1
        """
        if self._pours is None:
            return 0.0

        amount_poured = 0.0
        total_to_pour = 0.0
        for pour in self._pours:
            amount_poured += pour.current_amount
            total_to_pour += pour.recipe_amount

        return amount_poured / total_to_pour


    def __str__(self):
        return 'Drink {}: {}'.format(self.recipe.name, self.ID)
    def __repr__(self):
        return str(self)


def add_drink_pours(drink: Drink):
    """
    Adds pours from a drink to the waiting queue
    :param drink: obj to add to queue
    :return: None
    """
    for pour in drink.get_pours():
        add_pour(pour)