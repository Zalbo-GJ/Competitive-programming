class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        
        sub = [i for i in str(num)]
        
        ans = 0
        for i in range(k,len(sub)+1):
            s = sub[i-k:i]
            if int(''.join(s)) != 0 and num % int("".join(s)) == 0 :
                ans+=1
                
        return ans