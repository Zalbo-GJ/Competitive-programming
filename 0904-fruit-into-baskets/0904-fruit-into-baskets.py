class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        types = Counter()
        ans = variety = l = r = 0
        
        while r < len(fruits):
            
            if types[fruits[r]] == 0:
                variety+=1
            types[fruits[r]] += 1
            
            while variety > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    variety -= 1
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        return ans
            