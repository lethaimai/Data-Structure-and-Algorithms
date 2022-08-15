class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, new_node):  # to the end of the list
        current_node = self.head_node

        if not current_node:  # or you can write if current_node == None
            self.head_node = new_node

        while current_node:  # means while current_node != None
            next_node = current_node.get_next_node()
            if not next_node:  # means if next_node == None
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        current_node = self.head_node
        while(current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()
