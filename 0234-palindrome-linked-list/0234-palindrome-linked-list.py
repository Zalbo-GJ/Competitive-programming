# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        single = double = head
        half = []
        while double and  double.next:
            # half.append(single.val)
            single = single.next
            double = double.next.next
       
        while single:
            half.append(single.val)
            single = single.next
        
        half = half[::-1]
        
        curr = head
        for i in half:
            
            if  curr.val != i:
                return False
            
            curr = curr.next
            
        return True
        
        