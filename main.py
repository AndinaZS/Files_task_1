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

def get_shop_list_by_dishes(dishes, person_count):
    recipes = recipes_dict(os.path.join(os.getcwd(), 'recipes.txt'))
    result = {}
    for dish in dishes:
        recipe = recipes[dish]
        for el in recipe:
            ingredient, measure, number  = el['ingredient'], el['measure'], int(el['number'])
            result.setdefault(ingredient, {})
            result[ingredient] = {'measure': measure, 'number': result[ingredient].get('number', 0) + number * person_count}
    return result


pp(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))