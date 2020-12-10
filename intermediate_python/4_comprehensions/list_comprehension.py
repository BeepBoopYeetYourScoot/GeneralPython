# Можно перевесит как "облегчение списков"
# Позволяет генерировать списки, используя синтаксические конструкции
import random


def generate_random_array(length: int):
    """Функция генерирует список длины *length*,
        который состоит из случайных целых чисел"""
    temp = []
    for i in range(length):
        temp.append(random.randint(0, 101))
    return temp


# Этот алгоритм можно записать одним выражением

a = []
for x in range(10):
    a.append(x ** 2)

# Записывается следующим образом; При этом, comprehension работает быстрее, чем его развёрнутая форма.

comp_list = [x**2 for x in range(10)]

# Цикл for в python является циклом списочного типа, то есть, мы можем пробегать не по индексам, а непосредственно
# по элементам данного массива

alpha = generate_random_array(15)
beta = []
for x in alpha:
    if x % 2 == 0:
        beta.append(x ** 2)

# Данный алгоритм можно записать в одну строку:

c = [x for x in alpha if x % 2 == 0]

print(c)

