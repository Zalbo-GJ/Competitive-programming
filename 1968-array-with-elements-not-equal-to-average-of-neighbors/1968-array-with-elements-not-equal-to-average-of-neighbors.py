class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)-1):
            prev,curr,nex = nums[i-1],nums[i],nums[i+1]
            
            if prev < curr < nex or prev > curr > nex :
                nums[i],nums[i+1] = nums[i+1],nums[i]
        return nums