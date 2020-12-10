# Реализуем алгоритм сортировки вставками
import random


def generate_random_array(length: int):
    """Функция генерирует список длины *length*,
        который состоит из случайных целых чисел"""
    temp = []
    for i in range(length):
        temp.append(random.randint(0, 101))
    return temp


def insertion_sort(init_list: list):

    for i in range(len(init_list)):
        for j in range(i):
            if init_list[j] > init_list[i]:
                init_list[j], init_list[i] = init_list[i], init_list[j]

    return init_list


array = generate_random_array(15)
print(array)
print(insertion_sort(array))

