# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        single = double = head
        while double and double.next:
            single = single.next
            double = double.next.next
        middle = single
        
        #reverse half of the list
        
        prev = None
        while middle:
            nxt = middle.next
            middle.next = prev
            prev = middle
            middle = nxt
        
        i , j = head, prev
        
        while j :
            if i.val != j.val:
                return False
            i= i.next
            j= j.next
        return True
            
        
        