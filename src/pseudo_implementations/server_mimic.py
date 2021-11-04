"""
mimics a server. calls functions to test them
"""

import json

# should only have to import functions from main?
from src.recipe import recipe_parser


def get_recipe_str():
    with open("sample_data/example_recipes.json") as file:
        recipe_list = json.loads(file.read())
    return recipe_list[0]
    # recipe = recipe_parser.parse_recipe_str(json.dumps(recipe))
    # return recipe



def mimic_request_drink():
    """
    mimics a request for a drink from a UI app. makes calls to main.
    :return: None
    """
    req_recipe = get_recipe_str()




if __name__ == '__main__':
    serve_recipe_from_file()