class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def setHead(self, node):
        currHead = self.head
        currTail = self.tail
        if currHead == None and currTail == None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            node.next = currHead
            currHead.prev = node
            self.head = node
            self.length += 1

    def setTail(self, node):
        currHead = self.head
        currTail = self.tail
        if currHead == None and currTail == None:
            self.setHead(node)
        else:
            currTail.next = node
            node.prev = currTail
            self.tail = node
            self.length += 1

    def get(self, index):
        if index >= 0 and self.length > 0:
            curr = self.head
            count = 0
            while curr != None:
                if count == index:
                    return curr.val
                curr = curr.next
                count += 1
        return -1
