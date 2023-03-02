class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n == 1:
            return "0"
        
        return self.binary("0",n)[k-1]

    def binary(self, si,n):
        if n == 0:
            return si
        
        s = si + "1" + self.inverse(si)
        
        return self.binary(s,n-1)
        
    def inverse(self, s):
        l = 0
        r = len(s)-1
        s = list(map(str,s))
        
        while l<=r:
            
            if s[l] == "1":
                s[l] = "0"
            else:
                s[l] = "1"
            if l == r:
                break
            if s[r] == "1":
                s[r] = "0"
            else:
                s[r] = "1"
            
            s[l],s[r] = s[r], s[l]
            l+=1
            r-=1
            
        return "".join(s)           
            