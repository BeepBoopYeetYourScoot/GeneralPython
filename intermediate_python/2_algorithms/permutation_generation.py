# Алгоритм генерирует все возможные перестановки множества чисел
#


def find_in_prefix(num, pref):
    """Ищет num в pref и возвращает True, если такой есть;
    False, если такого нет"""

    for x in pref:
        if num == x:
            return True
    return False


def generate_permutations(c_sys_base: int, num_of_digits: int = -1, prefix = None):
    """ Генерирует все перестановки чисел в M позициях
    с префиксом prefix"""

    num_of_digits = c_sys_base if num_of_digits == -1 else num_of_digits
    prefix = prefix or []

    if num_of_digits == 0:
        print(*prefix)
        return

    for number in range(1, c_sys_base + 1):
        if find_in_prefix(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(c_sys_base, num_of_digits - 1, prefix)
        prefix.pop()


generate_permutations(6)
