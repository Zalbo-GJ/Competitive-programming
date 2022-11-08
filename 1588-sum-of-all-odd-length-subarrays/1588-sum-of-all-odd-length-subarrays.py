class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans= 0
        
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                
                if (j-i+1)%2 != 0 :
                    ans += sum(arr[i:j+1])
                 
        
        return ans