# Реализуем алгоритм линейного поиска в массиве
# Вообще, такой метод точно есть у типа данных list


def linear_search(array: list, N: int, x: int):
    """Осуществляет поиск числа x в массиве А
    от 0 до N-1 индекса включительно.
    Возвращает индекс элемента х в массиве А.
    Или -1, если такого значения не существует.
    Если значений несколько, то возвращает индекс
    первого из них.
    """

    for k in range(N):
        if array[k] == x:
            return k
    return -1


def test_linear_search():

    A1 = [1, 2, 3, 4, 5]
    m1 = linear_search(A1, 5, 8)
    if m1 == -1:
        print("test1 - ok")
    else:
        print("test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m2 = linear_search(A2, 5, -3)
    if m2 == 2:
        print("test2 - ok")
    else:
        print("test2 - fail")

    A3 = [1, 20, 22, 4, 20]
    m3 = linear_search(A3, 5, 20)
    if m3 == 1:
        print("test3 - ok")
    else:
        print("test3 - fail")


test_linear_search()


# Алгоритм данного поиска тривиален. Тем не менее, мы заморочились и описали функцию в полной мере
# Таким образом мы гарантировали, что функция делает ровно то, что нам нужно