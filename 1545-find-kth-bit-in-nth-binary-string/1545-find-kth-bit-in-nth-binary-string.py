class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        
        def inverse(st):
            ans=''
            for i in st:
                if i=='1':
                    ans+='0'
                else: 
                    ans+='1'
            return ans[::-1]
            
            
        def bString (s,ans):
            if len(ans) == n:
                return ans
            x = s+"1"+ inverse(s)
            ans.append(x)
            bString(x,ans)
            return ans[n-1][k-1]
        
        return bString('0',[])
