class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        seen = {}
        
        for i in range(len(s)-9):
            dna = s[i:i+10]
            
            if dna in seen:
                if not seen[dna]:
                    seen[dna] = True
                    ans.append(dna)
            else:
                seen[dna] = False
        return ans