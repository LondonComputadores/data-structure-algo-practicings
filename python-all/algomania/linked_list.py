import unittest


class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        self._head = Node(None)

    def insert_node_to_tail(self, node):
        self.tail().next = node

    def insert_node_to_head(self, node):
        if self._head.next:
            head_element = self._head
            node.next, head_element.next = head_element.next, node
        self._head.next = node

    def is_empty(self):
        return self._head.next is None

    def head(self):
        return self._head.next

    def tail(self):
        current = self._head
        while current.next:
            current = current.next
        return current
        

class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_first_node_to_tail(self):
        self.linked_list.insert_node_to_tail(Node('tail'))
        self.assertEqual('tail', self.linked_list.tail().value)

    def test_insert_first_node_to_head(self):
        self.linked_list.insert_node_to_head(Node('head'))
        self.assertEqual('head', self.linked_list.head().value)

    def test_insert_two_nodes_to_head(self):
        self.linked_list.insert_node_to_head(Node('head2'))
        self.linked_list.insert_node_to_head(Node('head1'))
        self.assertEqual('head1', self.linked_list.head().value)

    def test_insert_two_nodes_to_tail(self):
        self.linked_list.insert_node_to_tail(Node('tail2'))
        self.linked_list.insert_node_to_tail(Node('tail1'))
        self.assertEqual('tail1', self.linked_list.tail().value)

    def test_insert_nodes_to_head_and_tail(self):
        self.linked_list.insert_node_to_head(Node('head'))
        self.linked_list.insert_node_to_tail(Node('tail'))
        self.assertEqual('head', self.linked_list.head().value)
        self.assertEqual('tail', self.linked_list.tail().value)

    def test_is_empty_with_empty_linked_list(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_is_empty_with_two_nodes(self):
        self.linked_list.insert_node_to_head(Node('element1'))
        self.linked_list.insert_node_to_head(Node('element2'))
        self.assertFalse(self.linked_list.is_empty())


if __name__ == '__main__':
    unittest.main()