# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        single , double = head , head.next
        while double and double.next:
            single = single.next
            double = double.next.next
        curr = single.next
        single.next = node =  None
        
        while curr:
            nxt = curr.next
            curr.next = node
            node = curr
            curr = nxt
            
        h = head
        while node:
            tmp = node.next
            node.next = h.next
            h.next = node
            h = node.next
            node = tmp