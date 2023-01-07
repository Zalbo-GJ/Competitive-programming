class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        
        # first we save the index of each number in nums
        # we iterate over the operations and change the number with the other one 
        # by using the index we saved earlier
        d = {} 
        for indx, num in enumerate(nums):
            d[num] = indx

        print(d)
        for num, replacement in operations:
            
                indx = d[num]
                nums[indx] = replacement
                d[replacement] = indx
                del(d[num])
                
        return nums
            
            