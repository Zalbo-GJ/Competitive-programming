class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num = Counter(nums)
        h = []
        for key in num:
            heapq.heappush(h,(-num[key], key))
        
        r = []
        for _ in range(k):
            pop = heapq.heappop(h)
            r.append(pop[1])
        return r