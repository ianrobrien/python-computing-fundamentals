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

from src.util import collections
from unittest import TestCase


class CollectionsTest(TestCase):

    @classmethod
    def test_linkedlist_node(cls):
        node = collections.LinkedList()._Node_(100)
        assert node.next == None
        assert node.value == 100

    @classmethod
    def test_linkedlist(cls):
        linkedlist = collections.LinkedList()
        assert linkedlist.size == 0
        assert linkedlist.is_empty()

        linkedlist.add(10)
        linkedlist.add(20)
        linkedlist.add(30)
        linkedlist.add(40)

        assert linkedlist.size == 4
        assert linkedlist.contains(20)
        assert not linkedlist.is_empty()
        assert not linkedlist.contains(100)

        linkedlist.remove(40)
        linkedlist.remove(20)
        linkedlist.remove(10)
        linkedlist.remove(30)
        assert linkedlist.size == 0

    @classmethod
    def test_binarysearchtree(cls):
        bst = collections.BinarySearchTree()
        assert bst.size == 0
        assert bst.is_empty()
        assert not bst.contains(0)

        bst.add(50)
        assert not bst.contains(0)
        bst.add(25)
        bst.add(100)
        bst.add(150)
        bst.add(125)
        bst.add(12)

        assert bst.size == 6
        assert bst.contains(50)
        assert bst.contains(25)
        assert bst.contains(100)
        assert bst.contains(150)
        assert bst.contains(125)
        assert bst.contains(12)

    @classmethod
    def test_trie(cls):
        trie = collections.Trie()
        assert trie.size == 0

        trie.insert("hello")
        trie.insert("houses")
        trie.insert("hopes")

        assert trie.find("yikes") is None
        assert trie.find("hello") is not None
