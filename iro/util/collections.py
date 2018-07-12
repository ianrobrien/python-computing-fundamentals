class LinkedList:
    class _Node_:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.size = 0
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = self._Node_(value)
        else:
            next = self.root
            while (next.next is not None):
                next = next.next
            next.next = self._Node_(value)
        # Values can always be added to a collection
        self.size = self.size + 1

    def remove(self, value):
        if self.root is not None:
            if self.root.value == value:
                self.root = self.root.next
                self.size = self.size - 1
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


class BinarySearchTree:
    class _Node_:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, value):
        if self.root == None:
            self.root = self._Node_(value)
        else:
            def add_rec(node, value):
                if value < node.value:
                    if node.left == None:
                        node.left = self._Node_(value)
                    else:
                        add_rec(node.left, value)
                else:
                    if node.right == None:
                        node.right = self._Node_(value)
                    else:
                        add_rec(node.right, value)
            add_rec(self.root, value)
        # Values can always be added to a collection
        self.size = self.size + 1

    def contains(self, value):
        # Handle root cases
        if self.root == None:
            return False
        if self.root.value == value:
            return True

        def contains_rec(node, value):
            if node == None:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return contains_rec(node.left, value)
            else:
                return contains_rec(node.right, value)

        return contains_rec(self.root, value)
