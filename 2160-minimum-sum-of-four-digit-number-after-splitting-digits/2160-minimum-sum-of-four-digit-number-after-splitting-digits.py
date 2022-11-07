class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        num.sort()
        
        n1 = num[0]+num[3]
        n2 = num[1]+num[2]
        
        return int(n1)+int(n2)