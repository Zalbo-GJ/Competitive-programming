class Solution:
    def longestPrefix(self, s: str) -> str:
        
        lps = [0]
        i = 0
        j = 1
        
        while  j < len(s):
            if s[i] == s[j]:
                lps.append(i + 1)
                i += 1
                j += 1
            else:
                if i == 0:
                    lps.append(0)
                    j += 1
                else:
                    i = lps[i - 1]
        
        return  s[len(s) - lps[-1] : len(s)]