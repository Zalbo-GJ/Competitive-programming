# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ans = ListNode(0)
        head = ans
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            #add to new pointer
            
            val = v1+v2+carry
            
            carry = val/10
            val = val%10
            head.next = ListNode(val)
            
            #change pointers
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next