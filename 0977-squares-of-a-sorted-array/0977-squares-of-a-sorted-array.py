class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        for i in range(len(nums)):
            nums[i] *= nums[i]
        
        mini = nums[0]
        ind = 0
        for i in range(len(nums)):
            if nums[i] < mini:
                mini = nums[i]
                ind = i
        
        l = ind -1
        r = ind + 1
        result = [nums[ind]]
        while l>-1 or r<len(nums):
            
            if l < 0:
                while r < len(nums):
                    result.append(nums[r])
                    r+=1
                return result
            if r >= len(nums):
                while l>-1:
                    result.append(nums[l])
                    l-=1
                return result
            
            if nums[l] < nums[r]:
                result.append(nums[l])
                l-=1
            else:
                result.append(nums[r])
                r+=1
            
           
        return result
            
            
            