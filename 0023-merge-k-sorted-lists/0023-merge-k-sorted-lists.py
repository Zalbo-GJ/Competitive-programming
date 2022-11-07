# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h =[]
        for i,j in enumerate(lists):
            if j:
                heapq.heappush(h,(j.val,i,j))
        
        
        dummy = head = ListNode()
        while h:
            v,i,n = heapq.heappop(h)
            head.next = n
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i,lists[i]))
            head = head.next
        return dummy.next