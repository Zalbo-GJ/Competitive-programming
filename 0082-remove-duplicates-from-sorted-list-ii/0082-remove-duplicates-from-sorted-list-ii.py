# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            
            if head.val == head.next.val:
                
            
                while head and  head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                curr.next = head
            else:
                curr = curr.next
                head = head.next
                
        return dummy.next
                