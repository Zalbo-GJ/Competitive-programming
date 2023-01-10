class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num % 3 != 0:
            return []
        else:
            num /= 3
            
            return [num -1, num , num + 1]
        