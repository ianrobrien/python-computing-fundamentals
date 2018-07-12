class LinkedList:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.size = 0
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            next = self.root
            while (next.next is not None):
                next = next.next
            next.next = self.Node(value)
        self.size = self.size + 1

    def remove(self, value):
        if self.root is not None:
            if self.root.value == value:
                self.root = self.root.next
            else:
                next = self.root
                while next.next is not None:
                    if next.next.value == value:
                        next.next = next.next.next
                        self.size = self.size - 1
                        return
                    next = next.next

    def contains(self, value):
        next = self.root
        while (next is not None):
            if next.value == value:
                return True
            next = next.next
        return False

    def is_empty(self):
        return self.size == 0
