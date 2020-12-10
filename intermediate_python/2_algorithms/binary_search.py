# Бинарный поиск в массиве
# Требование к бинарному поиску - массив должен быть отсортирован
# Бинарный поиск позволяет реализовать прагматический смысл сортировки
# Постановка задачи: на выходе мы должны получить индексы левой и правой
# границы
# левая граница - элемент, который меньше текущего;
# правая граница - элемент, который больше искомого
# В случае, если элемента нет в массиве, левая и правая границы будут указывать
# на соседние индексы
# В случае, если элементов несколько, левая и правая границы будут указывать
# на диапазон, в котором содержатся данные элементы
# Скорость поиска - O(ln(N))


def left_bound(array: list, key):

    left = -1
    right = len(array)

    while right-left > 1:
        middle = (right + left) // 2

        if array[middle] < key:
            left = middle
        else:
            right = middle

    return left


def right_bound(array: list, key):

    left = -1
    right = len(array)

    while right-left > 1:
        middle = (right + left) // 2

        if array[middle] <= key:
            left = middle
        else:
            right = middle

    return right


def binary_search(array, key):

    left = left_bound(array, key)
    right = right_bound(array, key)
    diff = right - left

    if diff <= 1:
        return "There is no such entity"
    elif diff == 2:
        return left + 1
    else:
        return list(range(left + 1, right))


search_list = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9]
print(len(search_list))

print(binary_search(search_list, 7))
