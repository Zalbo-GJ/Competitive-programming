# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def cycle(head):
            slow = fast = head
            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
        
                if slow == fast:
                    return slow
        
            return None
        
        intersect = cycle(head)
        if intersect:
            start = head
            
            while intersect != start:
                start = start.next
                intersect = intersect.next
            
            return start
   
                