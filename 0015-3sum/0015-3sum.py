class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [] 
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            target = -nums[i]
            while l<r:
                val = nums[l]+nums[r]
                
                if val == target and [nums[i],nums[l],nums[r]] not in ans :
                    ans.append([nums[i],nums[l],nums[r]])
                if val > target:
                    r-=1
                else:
                    l+=1
        
        return  ans
                