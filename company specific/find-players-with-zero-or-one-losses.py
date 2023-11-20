class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ones = set()
        zeros = set()
        
        losers = set()
        
        for w, l in matches:
            
            if w not in ones and w not in losers:
                zeros.add(w)
                
            if l in ones:
                ones.remove(l)
                losers.add(l)

            elif l in zeros:
                zeros.remove(l)
                ones.add(l)
            elif l in losers:
                continue
            else:
                ones.add(l)
        
        return [sorted(zeros), sorted(ones)]
            
        