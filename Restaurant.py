import random
import numpy

dishes_string = 'spam, eggs,  tomato juice,   ham, eggs, eggs, ham, ham, ham, ham'
# dishes_string = input('Make order please \n')
dish_list = []

for dish in dishes_string.title().split(','):
    dish_list.append(dish.strip())
unique_dish_list = numpy.unique(dish_list)

for unique_dish_list in unique_dish_list:
    print(unique_dish_list.ljust(20, '.'), random.randint(0, 100), 'min')
