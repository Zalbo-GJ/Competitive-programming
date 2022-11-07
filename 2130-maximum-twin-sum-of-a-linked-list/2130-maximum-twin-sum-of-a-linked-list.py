# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head
        prev = None
        double = head
        single = head
        
        
        while double and double.next:
            single = single.next
            double = double.next.next
            
        half = single
        
        # reverse the second half
        while curr != half:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        ans = 0
        while prev:
            
            ans = max(ans,prev.val+half.val)
            prev = prev.next
            half = half.next
            
        return ans
            
            
            
        