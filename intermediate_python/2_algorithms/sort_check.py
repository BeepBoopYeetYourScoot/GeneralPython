# Необходимо проверить, отсортирован ли массив


def check_sorted(init_list, ascending = True):
    """Проверка отсортированности за О(N)"""

    # Для проверки сразу двух случаев: отсортирован по возврастанию и убыванию
    s = 2*int(ascending) - 1

    for i in range(len(init_list)-1):
        if s*init_list[i] > s*init_list[i+1]:
            return False

    return True


array = [5, 4, 3, 2, 1]

print(check_sorted(array, False))

