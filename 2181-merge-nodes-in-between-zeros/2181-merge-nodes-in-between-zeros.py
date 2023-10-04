# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr_dummy = dummy
        curr = head.next
        summ = 0
        while curr:
            if curr.val == 0:
                curr_dummy.next = ListNode()
                curr_dummy = curr_dummy.next
                curr_dummy.val = summ
                summ = 0
            
            summ += curr.val
            curr = curr.next
        
        
        return dummy.next