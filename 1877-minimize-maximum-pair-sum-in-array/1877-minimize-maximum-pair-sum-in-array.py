class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=0
        r= len(nums)-1
        maxPair=0
        while l<r:
            maxPair = max(maxPair,nums[l]+nums[r])
            l+=1
            r-=1
        return maxPair
        