import os
from pprint import pprint as pp

def recipes_dict(path):
    with open(path) as file:
        recipes_dict = {}
        for f in file:
            dish = f.strip()
            count = int(file.readline().strip())
            ingredients = []
            for _ in range(count):
                ingredient, number, measure = file.readline().strip().split('|')
                elem = {'ingredient': ingredient, 'number': number, 'measure': measure}
                ingredients.append(elem)
            recipes_dict[dish] = ingredients
            file.readline()
        return recipes_dict


recipes = recipes_dict(os.path.join(os.getcwd(), 'recipes.txt'))
pp(recipes)