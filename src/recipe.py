from typing import List, Tuple
from abc import ABC

class Recipe:
    ingredients: List[Tuple[str, float]]
    iter_index: int


    def __init__(self):
        self.ingredients = list()


    def __iter__(self):
        """
        Used for iterating over the ingredients
        :return:
        """
        self.iter_index = 0
        return self


    def __next__(self) -> str:
        """
        Get the next ingredient name in the list, but not the amount
        :return: next ingredient
        """
        self.iter_index += 1
        if self.iter_index > len(self.ingredients):
            raise StopIteration
        return self.ingredients[self.iter_index - 1][0]


    def __getitem__(self, item: str) -> float:
        """
        Get quantity of ingredient requested
        :param item: the ingredient
        :return: how much of that ingredient this recipe calls for
        """
        for ingr, amt in self.ingredients:
            if ingr == item:
                return amt

        return 0



class Recipe_Factory(ABC):
    @staticmethod
    def parse_recipe_str(recipe_str):
        """
        parses recipe string into recipe object. Subclass for whatever format of string youre using
        :param recipe_str: a string rep of a recipe - maybe json or xml
        :return: a recipe object
        """