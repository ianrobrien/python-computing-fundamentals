from iro.util import collections
from unittest import TestCase


class CollectionsTest(TestCase):

    @classmethod
    def test_linkedlist_node(cls):
        node = collections.LinkedList().Node(100)
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
        assert not linkedlist.contains(20)
        assert linkedlist.size == 2
