class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            return True
        
        for i in range(len(flowerbed)):
            
            
            if flowerbed[i] == 0:
                if i == 0 :
                    if flowerbed[i + 1] != 1:
                        n -= 1
                        flowerbed[i] = 1
                elif i == len(flowerbed) - 1 :
                    if flowerbed[i - 1] != 1:
                        n -= 1
                        flowerbed[i] = 1
                elif flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                    n -= 1
                    flowerbed[i] = 1
        
        return True if n < 1 else False
                
        