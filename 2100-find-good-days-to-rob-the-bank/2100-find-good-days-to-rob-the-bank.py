class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        ans= []
        n = len(security)
        forward = [0]*n
        back = [0]*n
        
        for i in range(1,n):
            if security[i-1]>= security[i]:
                forward[i]= forward[i-1]+1
        for i in range(n-2,-1,-1):
            if security[i] <= security[i+1]:
                back[i] = back[i+1]+1
        for i in range(n):
            if forward[i] >= time and back[i] >=time:
                ans.append(i)
        return ans