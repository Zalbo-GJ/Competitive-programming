class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        ans = [0]*len(l)
        
        for i in range(len(l)):
            
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            diff = arr[1]-arr[0]
            
            for j in range(1,len(arr)):
                
                if arr[j] - arr[j-1]==diff:
                    ans[i]= True
                else:
                    ans[i]= False
                    break
                    
        return ans