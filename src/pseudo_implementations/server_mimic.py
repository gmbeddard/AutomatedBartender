"""
mimics a server. calls functions to test them
"""

import json

from src.main import recipe_parser


def serve_recipe():
    with open("sample_data/example_recipes.json") as file:
        recipe_list = json.loads(file.read())
        recipe = recipe_list[0]
    recipe = recipe_parser.parse_recipe_str(json.dumps(recipe))
    print(recipe)
    for ingr in recipe:
        print(ingr, recipe[ingr])


if __name__ == '__main__':
    serve_recipe()