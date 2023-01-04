class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # split the words by space and put them in a list
        # find the max length from the strings
        # check if index is < len(string) if true
        # add to the string
        
        s = list(map(str, s.split(" ")))
        max_size = 0
        ans = []
        
        for i in s:
            max_size = max(max_size, len(i))
        
        for j in range(max_size):
            string = ""
            
            for i in s:
                if j >= len(i):
                    string += " "
                    continue
                string += i[j]
            ans.append(string.rstrip())
        return ans
                    
            
            
        