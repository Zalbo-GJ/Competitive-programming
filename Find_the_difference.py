from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        
        for i in t:
            if i in count:
                if count[i] ==1:
                    del(count[i])
                else:
                    count[i] -=1
            
            else:
                return i
        
