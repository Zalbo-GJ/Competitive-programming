# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
            less =[]
            greater = []
            curr = head
                
            while curr:
                if curr.val < x:
                    less.append(curr.val)
                else:
                    greater.append(curr.val)
                curr = curr.next
            
            curr = head
            for i in less:
                node = ListNode(i)
                curr.next = node
                curr = curr.next
                
            for i in greater:
                node = ListNode(i)
                curr.next = node
                curr = curr.next
            if head and  head.next:
                head = head.next
            
            return head
            
                
        