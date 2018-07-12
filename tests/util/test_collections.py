from iro.util import collections
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
        assert linkedlist.size == 1
        linkedlist.add(20)
        assert linkedlist.size == 2
        linkedlist.add(30)
        assert linkedlist.size == 3

        assert not linkedlist.contains(100)
        assert linkedlist.contains(20)
        assert not linkedlist.is_empty()

        linkedlist.remove(20)
        linkedlist.remove(10)
        linkedlist.remove(30)
        assert not linkedlist.contains(10)
        assert not linkedlist.contains(20)
        assert not linkedlist.contains(30)
        assert linkedlist.size == 0

    @classmethod
    def test_binarysearchtree(cls):
        bst = collections.BinarySearchTree()
        assert bst.size == 0
        assert bst.is_empty()
        assert not bst.contains(0)

        bst.add(50)
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
