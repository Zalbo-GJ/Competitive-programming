class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = [i for i in range(1,n+1)]
        k-=1
        def counter(idx):
            if len(arr)==1:
                return arr[0]
            idx = ((idx+k)%len(arr))
            
            del arr[idx]
            return counter(idx)
        return counter(0)