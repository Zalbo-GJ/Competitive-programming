class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr).values()
        count.sort()
        ans = freq = 0
        for i in range(len(count)-1,-1,-1):
            freq += count[i]
            ans+=1
            
            if freq >= len(arr)/2:
                
                return ans
        