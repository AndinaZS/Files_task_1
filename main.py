import os
from pprint import pprint as pp
path = os.path.join(os.getcwd(), 'recipes.txt')
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
    pp(recipes_dict)


