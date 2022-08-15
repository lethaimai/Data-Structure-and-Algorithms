from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList()] * self.array_size

    def hash(self, key):
        hash_code = sum(key.encode())
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for node in list_at_array:
            # Check if the key already exists in the LinkedList
            if node[0] == key: # The reason why you can get node[0] and not node.get_value()[0] is because the iter() dunder method of class LinkedList, it is using yield current_node.get_value()
                node[1] = value
                return
        # if not find the key through the list -> go to add the node into the list_at_array
        list_at_array.insert(payload)

        

    def retrieve(self, key):
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        list_at_index = self.array[array_index]

        # Iterate through the linked list and
        for node in list_at_index:
            if node[0] == key:
                return node[1]
        return None


########### Main ###########
blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])


print(blossom.retrieve("daisy"))



