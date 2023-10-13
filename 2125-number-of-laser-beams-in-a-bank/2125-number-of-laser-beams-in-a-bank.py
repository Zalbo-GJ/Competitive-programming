class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        ans = 0
        summ = 0
        last_wall = 0
       
        for idx in range(1,len(bank)):
            if not sum(list(map(int,bank[idx]))):
                continue
  
            summ = sum(list(map(int, bank[idx])))
            
            ans += (summ * sum(list(map(int, bank[last_wall]))))
            last_wall = idx
        
        return ans