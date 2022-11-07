# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(val=-9000,next=head)
        curr = head.next
        last_sorted = head
        
        while curr:
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                
                
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
                
            curr = last_sorted.next
        return dummy.next