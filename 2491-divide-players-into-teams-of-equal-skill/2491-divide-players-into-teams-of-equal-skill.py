class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        l = 1 
        r = len(skill)-2
        ans = skill[0] * skill[r+1]
        while l < r:
            
            if skill[l] + skill[r] == skill[l-1] + skill[r+1]:
           
                ans += skill[l] * skill[r]
            else: 
                return -1
            l += 1
            r -= 1
            
        
        
        return ans