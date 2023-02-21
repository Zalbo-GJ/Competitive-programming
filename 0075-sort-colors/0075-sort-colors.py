class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0]* 3
        
        for i in nums:
            count[i]+=1
        ind = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[ind] = i
                ind += 1
               
            
        
        