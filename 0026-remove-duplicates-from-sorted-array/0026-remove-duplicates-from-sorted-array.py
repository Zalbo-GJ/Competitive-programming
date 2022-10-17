class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        non = 0
        
        for i in range(1,len(nums)):
            if nums[non] != nums[i]:
                non+=1
                nums[non] = nums[i]
       
        return non+1