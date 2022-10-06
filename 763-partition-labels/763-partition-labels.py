class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_seen = {l:i for i,l in enumerate(s)}
        
        start = end = 0
        ans = []
        for i ,l in enumerate(s):
            end = max(end, last_seen[l])
            
            if i == end:
                ans.append(end-start+1)
                start = end+1
        return ans