from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """Agrega un elemento al final de la lista."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        """Agrega un elemento al inicio de la lista."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        """Obtiene un nodo en un índice específico con búsqueda optimizada."""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # Si el índice está en la primera mitad, busca desde el inicio
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        # Si está en la segunda mitad, busca desde el final
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def insert(self, index, value):
        """Inserta un valor en cualquier posición válida."""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True

    def remove(self, index):
        """Elimina un nodo en el índice indicado y re-engancha los punteros."""
        if index < 0 or index >= self.length:
            return None
        
        # Caso: Eliminar el único o el primero
        if index == 0:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1
            return temp
        
        # Caso: Eliminar el último
        if index == self.length - 1:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return temp

        # Caso: Eliminar en el medio
        node_to_remove = self.get(index)
        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev
        node_to_remove.next = None
        node_to_remove.prev = None
        self.length -= 1
        return node_to_remove