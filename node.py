class Node:
    """Clase que representa un nodo en una lista doblemente enlazada."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None