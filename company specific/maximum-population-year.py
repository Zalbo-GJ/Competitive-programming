class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        end = max(logs[x][1] for x in range(len(logs)))
        count = defaultdict(int)
        for year in range(min(logs)[0], end):
            for birth, death in logs:
                
                if year < death and year >= birth:
                    count[year] += 1
        ans = logs[0][0]
        
        for date, ppl in count.items():
            if ppl > count[ans]:
                ans = date
            elif ppl == count[ans] and ans > date:
                ans = date

        return ans
        