class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        c = Counter(changed)
        if len(changed) % 2 :
            return []
        
        for x in sorted(c):
            if c[x] > c[x*2]:
                return []
            c[x*2] -= c[x] if x else c[x]/2
        return c.elements()