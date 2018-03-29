import random
import numpy

def random_cook_time():
    return random.randint(0, 100)

dishes_string = 'spam, eggs,  tomato juice,   ham, eggs, eggs, ham, ham, ham, ham'
# dishes_string = input('Make order please \n')
dish_list = []

for dish in dishes_string.title().split(','):
    dish_list.append(dish.strip())
unique_dish_list = numpy.unique(dish_list)

for unique_dish in unique_dish_list:
    if unique_dish != '':
        print(unique_dish.ljust(20, '.'), random_cook_time(), 'min')
