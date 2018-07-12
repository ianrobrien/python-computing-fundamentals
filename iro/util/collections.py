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
            def add_rec(_Node_, value):
                if value < _Node_.value:
                    if _Node_.left == None:
                        _Node_.left = self._Node_(value)
                    else:
                        add_rec(_Node_.left, value)
                else:
                    if _Node_.right == None:
                        _Node_.right = self._Node_(value)
                    else:
                        add_rec(_Node_.right, value)
            add_rec(self.root, value)
        # Values can always be added to a collection
        self.size = self.size + 1

    def contains(self, value):
        # Handle root cases
        if self.root == None:
            return False
        if self.root.value == value:
            return True

        def contains_rec(_Node_, value):
            if _Node_ == None:
                return False
            if _Node_.value == value:
                return True
            if value < _Node_.value:
                return contains_rec(_Node_.left, value)
            else:
                return contains_rec(_Node_.right, value)

        return contains_rec(self.root, value)
