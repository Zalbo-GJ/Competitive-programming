class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        pos, idx = 0,0
        
        while idx < len(chars):
            chars[pos] = chars[idx]
            count = 1
            
            while idx < len(chars)-1 and chars[idx] == chars[idx+1]:
                idx+=1
                count+=1
            if count>1:
                for ch in str(count):
                    pos += 1
                    chars[pos] = ch
            pos+=1
            idx +=1
        
        return pos
                