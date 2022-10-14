class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.invert(0,len(nums)-1,nums)
        k %= len(nums)
        self.invert(0,k-1,nums)
        self.invert(k,len(nums)-1,nums)
    
    
    def invert(self,l,r,arr):
        
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            
            r-=1
            l+=1
        return arr