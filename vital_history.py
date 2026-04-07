from node import Node

class VitalHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length: return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index): temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1): temp = temp.prev
        return temp

    def insert(self, index, data):
        if index < 0 or index > self.length: return False
        if index == 0: return self.prepend(data)
        if index == self.length: return self.append(data)
        new_node = Node(data)
        before = self.get(index - 1)
        after = before.next
        new_node.prev, new_node.next = before, after
        before.next = after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length: return None
        if index == 0:
            temp = self.head
            if self.length == 1: self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1
            return temp
        if index == self.length - 1:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return temp
        node_to_remove = self.get(index)
        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev
        self.length -= 1
        return node_to_remove.data