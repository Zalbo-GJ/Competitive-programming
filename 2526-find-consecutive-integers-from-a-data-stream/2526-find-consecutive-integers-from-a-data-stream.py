class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        self.consec_length  = 0
        
        

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == self.value:
            self.consec_length += 1
        else:
            self.consec_length = 0
        
        if self.consec_length >= self.k:
            return True
        return False
            
        
        
    

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)