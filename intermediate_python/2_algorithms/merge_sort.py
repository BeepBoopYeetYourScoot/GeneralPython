# На любой выборке сложность алгоритма - O(N*ln(N)
# Сортирующее действие выполняется на обратном ходу рекурсии
# Требует дополнительной памяти

# Сортирующее действие - слияние отсортированных массивов в один

# Сортировка называется устойчивой, если она не меняет порядок равных элементов

import random


def generate_random_array(length: int):
    """Функция генерирует список длины *length*,
        который состоит из случайных целых чисел"""
    temp = []
    for i in range(length):
        temp.append(random.randint(0, 101))
    return temp


# Можно реализовать алгоритм merge sort таким образом, чтобы сортировке
# поддавалась только отдельная часть массива с позициями
# (начало сортировки; середина; конец)


def merge_sort(init_list: list, start_ind: int, finish_ind: int):

    # Сначала сортируем

    len_c = finish_ind - start_ind
    middle_ind = start_ind + len_c//2

    if len_c <= 1:
        return

    a = init_list[start_ind:middle_ind]
    b = init_list[middle_ind:finish_ind+1]

    merge_sort(a, 0, middle_ind)
    merge_sort(b, middle_ind, finish_ind)

    # Потом сливаем

    i = 0
    j = 0
    k = start_ind

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            init_list[k] = a[i]
            i += 1
        else:
            init_list[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        init_list[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        init_list[k] = b[j]
        j += 1
        k += 1

    return init_list


rand_list = generate_random_array(15)

print(rand_list)
print(merge_sort(rand_list, 0, 5))

