# Быстрая сортировка Тони Хоара
# На средней выборке сложность алгоритма  - O(N*ln(N))
# На отдельных выборках, в худшем случае, сложность - О(N^2)
# Сортирующее действие выполняется на прямом ходу рекурсии
# Может быть реализована без дополнительной памяти
# Относится к алгоритмам вида "Разделяй и властвуй"
import random

# В питоне используется комбинация из merge sort и insert sort для достижения
# наиболее благоприятной асимптотики и называется timsort


def generate_random_array(length: int):
    """Функция генерирует список длины *length*,
        который состоит из случайных целых чисел"""
    temp = []
    for i in range(length):
        temp.append(random.randint(0, 101))
    return temp


def quick_sort(init_list: list, start_ind: int, finish_ind: int):

    if len(init_list) <= 1:
        return

    barrier = init_list[0]

    L, M, R = [], [], []

    # Можно реализовать алгоритм без потребления дополнительной памяти
    # На данный момент он будет потреблять дополнительно init_list памяти

    # Сначала делим массив

    for x in init_list:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    k = 0
    # Сложение списков также не эффективно по памяти и можно, например,
    # воспользоваться срезами

    quick_sort(L, 0, len(L))
    quick_sort(R, 0, len(R))

    # Потом сортируем разделённые элементы

    for x in L + M + R:
        init_list[k] = x
        k += 1

    return init_list


array = generate_random_array(15)
print(array)
print(quick_sort(array, 0, 5))



