_name_='Кувалдин Е.A.'


print('Задача №1')
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
import math
a, b = [], []
for i in range(10):
    a.append(random.randint(1, 10))
print('Исходный список: ', a)
b = list(map(lambda x: x**2, a))
print('Список результатов: ', b)

print('Задача №2')
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruitsFirst = ['Айва', 'Банан', 'Яблоко', 'Апельсин', 'Груша', 'Авокадо', 'Гранат']
fruitsSecond = ['Арбуз', 'Банан', 'Киви', 'Апельсин', 'Кокос', 'Авокадо', 'Фейхоа']
reslist = []
for i in fruitsFirst:
    for r in fruitsSecond:
        if i in r:
            reslist.append(i)
print('Список фруков 1: ', fruitsFirst)
print('Список фруктов 2: ', fruitsSecond)
print('Неуникальные фрукты: ', reslist)

print('Задача №3')
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
w, t = [], []
for i in range(30):
    w.append(random.randint(-100, 100))
for i in w:
    if i % 3 == 0 and i % 4 != 0 and i > 0:
        t.append(i)
print('Исходный список: ', w)
print('Список результата: ', t)