# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        
        single , double = head , head.next
        while double and double.next:
            single = single.next
            double = double.next.next
        r = single.next
        single.next = None
        left = self.sortList(head)
        right = self.sortList(r)
        
        return self.merge(left,right)
        
        
    def merge(self, l,r):
        if not l or not r:
            return 1 or r
        dummy = curr = ListNode(0)
        
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        curr.next = l or r
        return dummy.next