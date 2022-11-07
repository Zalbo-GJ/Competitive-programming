# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        single = double = head
        while double and double.next:
            single = single.next
            double = double.next.next  # 2 steps each so when double finishes single will be middle
        return single
