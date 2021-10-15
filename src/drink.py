from uuid import UUID, uuid4
from typing import List, Optional

from recipe import Recipe
from pour import Pour
from main import make_pour


class Drink:
    recipe: Recipe
    ID: UUID
    pours: Optional[List[Pour]]


    def __init__(self, recipe: Recipe):
        """
        :param recipe: recipe object
        """
        self.recipe = recipe
        self.ID = uuid4()
        self.pours = None


    def _make_pours(self):
        """
        initializes pour list
        :return: None
        """
        self.pours = list()
        for ingredient in self.recipe:
            self.pours.append(make_pour(ingredient, self.recipe[ingredient]))


    def get_pours(self) -> List[Pour]:
        """
        Get a list of pours needed to make this drink.
        :return: list of pours
        """
        if self.pours is None:
            self._make_pours()
        return self.pours


    def get_status(self) -> float:
        """
        Get's this drink's current progress: sum amount poured / total to pour
        :return: float btwn 0 and 1
        """
        if self.pours is None:
            return 0.0

        amount_poured = 0.0
        total_to_pour = 0.0
        for pour in self.pours:
            amount_poured += pour.current_amount
            total_to_pour += pour.recipe_amount

        return amount_poured / total_to_pour