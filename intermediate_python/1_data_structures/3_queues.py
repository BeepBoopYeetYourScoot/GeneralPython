# Используются для распределения потоков и для применения многопоточности
# Как и стеки, хранят инфу последовательным образом. Однако, очереди хранят её
# по принципу FIFO - First IN - First OUT (как и обычная очередь


class Queue:
    """Представялет собой класс, с помощью которого можно
    реализовать структуру данных "очередь" """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавить элемент в конец очереди """
        return self.items.insert(0, item)

    def dequeue(self):
        """Удалить первый элемент в очереди"""
        return self.items.pop()

    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return self.items == []

    def top(self):
        """Возвращает первый элемент в очереди"""
        return self.items[-1]


A = Queue()

for i in range(10):
    A.enqueue(i)

print(A.items)

for i in range(3):
    A.dequeue()

print(A.items)

