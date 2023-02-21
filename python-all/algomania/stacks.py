from linked_list import LinkedList, Node
import unittest


def print_linked_list(linked_list):
    node = linked_list.head()
    while node:
        print(node.value, end=' ')
        node = node.next
    print(' ')

def print_reversed_linked_list(linked_list):
    stack =[]
    node = linked_list.head()
    while node:
        stack.append(node.value)
        node = node.next
    while stack:
        print(stack.pop(), end=' ')
    print(' ')


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_reversed_list(self):
        self.linked_list.insert_node_to_tail(Node('1'))
        self.linked_list.insert_node_to_tail(Node('2'))
        self.linked_list.insert_node_to_tail(Node('3'))
        self.linked_list.insert_node_to_tail(Node('4'))
        self.linked_list.insert_node_to_tail(Node('5'))

        print_linked_list(self.linked_list)
        print_reversed_linked_list(self.linked_list)


if __name__ == '__main__':
    unittest.main()