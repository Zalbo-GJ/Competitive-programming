# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        curr = head.next
        last_sorted = head
        
        while curr:
            if curr.val >= last_sorted.val:
                
                last_sorted = last_sorted.next
            else:
                
                prev = dummy
                while prev.next and prev.next.val <= curr.val:
                    prev = prev.next
                    
                last_sorted.next = curr.next
                nxt = prev.next
                prev.next = curr
                curr.next = nxt
            
            curr = last_sorted.next
        
        return dummy.next
        
