import random


def generate_random_array(length: int):
    """Функция генерирует список длины *length*,
        который состоит из случайных целых чисел"""
    temp = []
    for i in range(length):
        temp.append(random.randint(0, 101))
    return temp


array = generate_random_array(10)
print(array)


def bubble_sort(array_to_sort: list):
    """Функция реализует алгоритм сортировки пузырьком.
        Принимает на вход только существующие в Python
        типы массивов"""

    for n in range(1, len(array_to_sort)):
        for m in range(len(array_to_sort) - n):
            if array_to_sort[m] > array_to_sort[m+1]:
                array_to_sort[m], array_to_sort[m+1] = array_to_sort[m+1], array_to_sort[m]

    return array_to_sort


print(bubble_sort(array))

