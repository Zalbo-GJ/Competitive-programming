# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        li = []
        curr = head
        
        while curr != None:
            li.append(curr.val)
            curr = curr.next
        li = li[::-1]
        head = ListNode()
        curr = head
        for i in li:
            node = ListNode(i)
            curr.next = node
            curr = curr.next
        head = head.next
        
        
        
        return head            
            