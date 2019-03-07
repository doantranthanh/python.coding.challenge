import unittest
import doubly_linked_list


class Test_DoublyLinkedList_Implementation(unittest.TestCase):
    def test_empty_list_when_init_doubly_linked_list(self):
        dbLList = doubly_linked_list.DoublyLinkedList()
        self.assertEqual(dbLList.length, 0)
        self.assertEqual(dbLList.head, None)
        self.assertEqual(dbLList.tail, None)

    def test_set_head_implementation(self):
        first_node = doubly_linked_list.Node(1)
        second_node = doubly_linked_list.Node(2)
        dbLList = doubly_linked_list.DoublyLinkedList()
        dbLList.setHead(first_node)
        dbLList.setHead(second_node)
        firstNode_Val = dbLList.get(0)
        secondNode_Val = dbLList.get(1)
        self.assertEqual(dbLList.length, 2)
        self.assertEqual(second_node.val, firstNode_Val)
        self.assertEqual(first_node.val, secondNode_Val)

    def test_set_tail_implementation(self):
        first_node = doubly_linked_list.Node(1)
        second_node = doubly_linked_list.Node(2)
        last_node = doubly_linked_list.Node(3)
        dbLList = doubly_linked_list.DoublyLinkedList()
        dbLList.setHead(first_node)
        dbLList.setHead(second_node)
        dbLList.setTail(last_node)
        self.assertEqual(dbLList.length, 3)

    def test_insert_before_implementation(self):
        node_insert = doubly_linked_list.Node(1)
        dbLList = doubly_linked_list.DoublyLinkedList()


if __name__ == "__main__":
    unittest.main()
