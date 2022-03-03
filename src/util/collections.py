# Copyright (c) 2018-present, Ian R. O'Brien
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################


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
        self.size += 1

    def remove(self, value):
        if self.root is not None:
            if self.root.value == value:
                self.root = self.root.next
                self.size -= 1
            else:
                next = self.root
                while next.next is not None:
                    if next.next.value == value:
                        next.next = next.next.next
                        self.size -= 1
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
        self.size += 1

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
            return contains_rec(node.left, value) if value < node.value else contains_rec(node.right, value)

        return contains_rec(self.root, value)


class Trie:
    class _Node_:
        def __init__(self):
            self.children = {}
            self.value = None

    def __init__(self):
        self.size = 0
        self.root = self._Node_()

    def insert(self, value):
        node = self.root
        index_last_char = None
        for index_char, char in enumerate(value):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break
        if index_last_char is not None:
            for char in value[index_last_char:]:
                node.children[char] = self._Node_()
                node = node.children[char]

        node.value = value
        self.size += 1

    def find(self, value):
        node = self.root
        for char in value:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value
