class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashset = set()
        
        for i in range(len(nums)):
            if i > k:
                hashset.remove(nums[i-(k+1)])
            
            if  nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False