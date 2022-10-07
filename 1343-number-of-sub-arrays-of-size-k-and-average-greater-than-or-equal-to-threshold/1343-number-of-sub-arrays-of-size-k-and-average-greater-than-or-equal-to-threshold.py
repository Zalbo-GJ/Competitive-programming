class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        sub = sum(arr[:k-1])
        count = 0
    
        for i in range(k-1,len(arr)):
            
            sub += arr[i]
            if sub/k >= threshold:
                count+=1
            sub-= arr[i-k+1]
        return count