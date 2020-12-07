# Стеком называется тип данных, организованный по принципу LIFO: Last IN - First OUT
# Стеки можно представлять в виде сложенных в стопку книг или тарелок:
# последняя книга/тарелка, которую ты положишь в стопку, будет первой, которую ты сможешь
# забрать.
# Основные операции со стеками:


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


my_list = [1, 2, 3, 4, 5]

stack = Stack()

for num in my_list:
    stack.push(num)

stack.push(7)

empty_list = []
# empty_stack = Stack(empty_list)

print(stack.items)
print(stack.is_empty())
# print(empty_stack.is_empty())
