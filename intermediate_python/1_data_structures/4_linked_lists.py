# Класс содержит базовые операции структуры, однако, написаны они через жопу, поэтому
# класс, скорее всего, не работает.

class LinkedList:

    def __init__(self):
        self.head = None

    def contains(self, item):
        last_item = self.head
        while last_item:
            if item == last_item.item:
                return True
            else:
                last_item = last_item.next_item
        return False

    def add_to_end(self, new_item):
        new_node = Node(new_item)
        if self.head is None:
            self.head = new_item
            return
        last_item = self.head
        while last_item.next_item:
            last_item = last_item.next_item
        last_item.next_item = new_node

    def get_node_by_index(self, node_index):
        last_item = self.head
        item_index = 0
        while item_index <= node_index:
            if item_index == node_index:
                return last_item.item
            item_index += 1
            last_item = last_item.next_item

    def remove_node(self, removed_item):
        head_item = self.head

        if head_item is not None:
            if head_item.item == removed_item:
                self.head = head_item.next_item
                head_item = None
                return
        while head_item is not None:
            if head_item.item == removed_item:
                break
            last_item = head_item
            head_item = head_item.next_item
        if head_item is None:
            return
        # last_item.next_item = head_item.next_item
        # head_item = None


class Node:

    def __init__(self, item=None):
        self.item = item
        self.prev_item = None
        self.next_item = None




string = """
Кроваво-черное ничто 
пустилось вить систему клеток, 
связанных внутри, клеток, 
связанных внутри, клеток в едином стебле 
и явственно, до жути на фоне тьмы 
ввысь белым бил фонтан"""

array = string.split()

print(array)
