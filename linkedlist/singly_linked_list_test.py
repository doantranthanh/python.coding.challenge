import unittest
import singly_linked_list


class Test_Singly_Linked_List(unittest.TestCase):
    def test_add_to_tail_implementation(self):
        first_list = singly_linked_list.SinglyLinkedList()
        first_list.addToHead(2)
        first_list.addToHead(4)
        first_list.addToHead(3)
        second_list = singly_linked_list.SinglyLinkedList()
        second_list.addToHead(5)
        second_list.addToHead(6)
        second_list.addToHead(4)
        solution = singly_linked_list.Solution()
        sumList = solution.addTwoNumbers(first_list, second_list)
        self.assertEqual(sumList.get(0), 7)
        self.assertEqual(sumList.get(1), 0)
        self.assertEqual(sumList.get(2), 8)


if __name__ == "__main__":
    unittest.main()
