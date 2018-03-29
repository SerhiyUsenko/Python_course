import random
import numpy

class Dish:
    def __init__(self, name):
        self.name = name
    name_dish = 'tomato'

v = Dish('white wine')

def random_cook_time():
    return random.randint(0, 100)

def to_print():
    print(unique_dish.ljust(20, '.'), random_time(), 'min')
    pass

dishes_string = v.name + ', ' + Dish.name_dish + ', spam, eggs,  tomato juice,,,,   ham, eggs, eggs, ham, ham, ham, ham'
# dishes_string = input('Make order please(separated by comma) \n')
dish_list = []

for dish in dishes_string.title().split(','):
    dish_list.append(dish.strip())
unique_dish_list = numpy.unique(dish_list)

for unique_dish in unique_dish_list:
    if unique_dish != '':
        to_print()
