__author__ = 'Шварева Софья Дмитриевна'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

shopping_list = ["яблоко", "банан", "киви", "арбуз"]
for i in range(len(shopping_list)):
    print('{}.'.format(i+1), '{:>6}'.format(shopping_list[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


list1 = [1, 6, 3, 8, 4, 9, 0, 2, 1, 8]
list2 = [6, 3, 7, 0, 7, 8]
print(list1, list2)
for element in list2:
    if element in list1:
        while element in list1:
            list1.remove(element)
print(list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_of_numbers = [1, 6, 3, 8, 4, 9, 0, 2, 1, 8]
new_list_of_numbers = []
for number in list_of_numbers:
    if number % 2 == 0:
        new_list_of_numbers.append(number / 4)
    else:
        new_list_of_numbers.append(2 * number)
print('Исходный список: ', list_of_numbers, '; \nНовый список: ', new_list_of_numbers)
