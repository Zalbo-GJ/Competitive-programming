class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-i for i in nums]
        heapq.heapify(nums)
        
        while k >1:
            heapq.heappop(nums)
            k-=1
        return -heapq.heappop(nums)