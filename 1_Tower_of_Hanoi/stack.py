from node import Node


class Stack:
    def __init__(self, name):
        self.name = name
        self.limit = 1000
        self.size = 0
        self.top_item = None

    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.has_space():
            new_item = Node(value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
        else:
            print("No more room")

    def pop(self):
        if not self.is_empty():
            removed_item = self.top_item
            self.top_item = removed_item.get_next_node()
            self.size -= 1
            return removed_item.get_value()
        print("This stack is totally empty")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def print_items(self):
        pointer = self.top_item
        print_list = []
        while (pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))
