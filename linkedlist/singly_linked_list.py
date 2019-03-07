class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addToTail(self, val):
        if self.head == None:
            self.addToHead(val)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            end_node = ListNode(val)
            curr.next = end_node

    def sumUp(self):
        sum = 0
        curr = self.head
        if curr != None:
            count = 0
            while curr != None:
                sum += curr.val * 10 ** count
                curr = curr.next
                count += 1
        return sum

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.val)

    def get(self, index):
        if index >= 0 and self.head != None:
            count = 0
            curr = self.head
            while curr != None:
                if count == index:
                    return curr.val
                curr = curr.next
                count += 1
        return -1


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1, l2):
        sum = l1.sumUp() + l2.sumUp()
        result = SinglyLinkedList()
        while sum > 0:
            val = sum % 10
            result.addToTail(val)
            sum = sum // 10
        return result
