class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str,nums)
        for _ in range(len(nums)):
            for j in range(len(nums)-1):
                if int(nums[j]+nums[j+1]) < int(nums[j+1]+nums[j]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        
        return '0' if int( "".join(nums))==0 else ''.join(nums)
