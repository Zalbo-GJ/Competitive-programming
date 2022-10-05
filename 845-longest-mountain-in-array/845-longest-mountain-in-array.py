class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        start = ans = 0
        
        while start < n:
            end = start
            if end + 1 < n and arr[end] < arr[end+1]:
                while end + 1 < n and arr[end] < arr[end+1]:
                    end +=1
                
                if end + 1 < n and arr[end] > arr[end+1]:
                    while end + 1 < n and arr[end] > arr[end+1]:
                        end += 1
                    
                    ans = max(ans, end-start+1)
            
            start = max(end, start+1)
        return ans