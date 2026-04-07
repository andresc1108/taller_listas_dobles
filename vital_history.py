from node import Node

class VitalHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_record(self, vital_sign):
        new_node = Node(vital_sign)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def remove_record(self, index):
        if index < 0 or index >= self.length: return None
        if index == 0:
            temp = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1
            return temp
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        if curr == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.length -= 1
        return curr.data