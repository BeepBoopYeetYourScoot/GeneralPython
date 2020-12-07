# Кастомный модуль, чтобы рассмотреть базовые принципы работы с ними

print('Imported custom module. hehe hoho ...')

test = 'Test String'


def find_index(list_to_search, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(list_to_search):
        if value == target:
            return i

    return -1


