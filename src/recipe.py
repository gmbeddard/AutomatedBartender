from typing import List, Tuple, Type
from abc import ABC, abstractmethod
import json


class Recipe:
    name: str
    _ingredients: List[Tuple[str, float]]
    _iter_index: int

    def __init__(self):
        self._ingredients = list()


    def __iter__(self):
        """
        Used for iterating over the ingredients, eg. for ingredient in recipe: ...
        :return:
        """
        self._iter_index = 0
        return self


    def __next__(self) -> str:
        """
        Get the next ingredient name in the list, but not the amount
        :return: next ingredient
        """
        self._iter_index += 1
        if self._iter_index > len(self._ingredients):
            raise StopIteration
        return self._ingredients[self._iter_index - 1][0]


    def __getitem__(self, item: str) -> float:
        """
        Get quantity of ingredient requested, eg recipe[ingredient] -> 0.8
        :param item: the ingredient
        :return: how much of that ingredient this recipe calls for
        """
        for ingr, amt in self._ingredients:
            if ingr == item:
                return amt

        return 0


    def __str__(self):
        base = '{}: '.format(self.name)
        for ingredient in self:
            base += '{}: {} mL, '.format(ingredient, self[ingredient])
        return base.removesuffix(', ')


class Recipe_Factory(ABC):
    @staticmethod
    @abstractmethod
    def parse_recipe_str(recipe_str: str) -> Recipe:
        """
        parses recipe string into recipe object. Subclass for whatever format of string youre using
        :param recipe_str: a string rep of a recipe - maybe json or xml
        :return: a recipe object
        """


# Legitimate recipe factories. Im just gonna make json for now for fun
# TODO add name attribute to ingredients?
class JSON_Recipe_Factory(Recipe_Factory):
    @staticmethod
    def parse_recipe_str(recipe_str: str) -> Recipe:
        """
        Uses python's json parser to decode recipe_str.
        does not handle any malformed json errors. you gotta do that yourself
        :param recipe_str: recipe in json format
        :return: Recipe object
        """
        recipe_json_obj = json.loads(recipe_str)
        recipe_obj = Recipe()

        recipe_obj.name = recipe_json_obj['recipe_name']
        # sort list by index
        recipe_json_obj['ingredients'].sort(key=lambda ingr: ingr['index'])

        # get ingrs from list
        for ingredient_dict in recipe_json_obj['ingredients']:
            recipe_obj._ingredients.append((
                ingredient_dict['id'].upper(),
                ingredient_dict['qty']
            ))

        return recipe_obj


# set which recipe parser we are going to use
recipe_parser: Type[Recipe_Factory] = JSON_Recipe_Factory