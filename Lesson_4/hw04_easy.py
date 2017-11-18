__author__ = 'Шварева Софья Дмитриевна'

# Все задачи текущего блока решите с помощью генераторов списков!

print('Задание-1: ')
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

from random import randint

random_list = [randint(-100, 100) for _ in range(10)]
list_of_squares = [x*x for x in random_list]
print(random_list)
print(list_of_squares)


print('Задание-2:')
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['яблоко', 'банан', 'манго', 'персик', 'ананас']
fruits2 = ['манго', 'апельсин', 'банан',  'ананас']
fruits3 = [fruit for fruit in fruits1 if fruit in fruits2]
print(fruits3)


print('Задание-3:')
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

randomlist = [randint(-100, 100) for _ in range(15)]
print(randomlist)
new_list = [element for element in randomlist if (element % 3 == 0) and (element > 0) and (element % 4 != 0)]
print(new_list)
