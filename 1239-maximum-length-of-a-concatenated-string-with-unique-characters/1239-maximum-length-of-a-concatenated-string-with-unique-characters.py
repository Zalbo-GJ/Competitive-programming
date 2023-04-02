class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        max_len = 0
        temp = []
        
        def recur(ind):
            nonlocal max_len
            
            if ind == len(arr):
                string = "".join(temp)
                count = Counter(string)
                if len(count) == sum(count.values()):
                    max_len = max(max_len,len(string))
                
                return
            
            temp.append(arr[ind])
            recur(ind + 1)
            temp.pop()
            recur(ind + 1)
        
        recur(0)
        
        return max_len
        