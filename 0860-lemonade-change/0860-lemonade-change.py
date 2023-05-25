class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        tens = 0
        fives = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10 and fives >= 1:
                tens += 1
                fives -=1
            elif bill == 20 and fives >= 1 and tens >= 1:
                tens -= 1
                fives -= 1
            elif bill == 20 and fives >= 3:
                fives -= 3
            else:
                return False
        
        return True