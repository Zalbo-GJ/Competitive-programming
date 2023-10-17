# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = []
        
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        num2 = []
        
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        summ = int("".join(num1)) + int("".join(num2))
        
        summ = list(str(summ))
        
        head = ListNode()
        dummy = head
        
        for num in summ:
            head.next = ListNode()
            head.next.val = num
            head = head.next
        
        return dummy.next