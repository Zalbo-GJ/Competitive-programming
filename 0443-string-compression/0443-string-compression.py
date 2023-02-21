class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        pos = 0
        idx = 0
        
        while idx < len(chars):
            chars[pos] = chars[idx]
            count = 1
            
            while idx+1 < len(chars) and chars[idx] == chars[idx+1]:
                idx += 1
                count += 1
            if count>1:
                for ch in str(count):
                    pos += 1
                    chars[pos] = ch
            pos += 1
            idx += 1 
        
        return pos
                
        