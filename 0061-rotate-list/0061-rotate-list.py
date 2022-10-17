# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        
        if head is None or head.next is None:
            return head
       
		
        
	
        curr = head
        length = 0
        while curr and curr.next:
            length += 1
            curr = curr.next
        length += 1
        
		
        k = k%length
        
		
        if k == length or k == 0:
            return head
           
		
        prev = head
        for i in range(1, length-k):
            prev = prev.next
			
		
        curr.next = head
        head = prev.next
        prev.next = None
		
        return head