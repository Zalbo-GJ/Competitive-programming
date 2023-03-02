class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        1.we count the types fo fruits in the window, if types > 2 we shrink else we expand
        2.we count the max(no_fruits) in window when types <= 2
        """
        
        l = 0
        inBasket = 0
        dic = {}
        
        for r in range(len(fruits)):
            
            if fruits[r] in dic:
                dic[fruits[r]] += 1
            else :
                dic[fruits[r]] = 1
            
            while len(dic) > 2:
                dic[fruits[l]] -= 1   
                if dic[fruits[l]] == 0:
                    del(dic[fruits[l]])
                l += 1
            
            inBasket = max(inBasket, r-l+1)
        
        return inBasket
            
            
            