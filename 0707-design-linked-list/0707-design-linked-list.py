class MyLinkedList(object):

    def __init__(self):
        
        self.head = None
        self.size = 0

    def get(self, index):
       
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
       
        node = ListNode(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        
        curr = self.head
        if curr is None:
            self.head = ListNode(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = ListNode(val)

        self.size += 1

    def addAtIndex(self, index, val):
        
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = ListNode(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
       
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)