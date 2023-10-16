class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = defaultdict(list)
        
        for idx in range(len(groupSizes)):
            count[groupSizes[idx]].append(idx)
        ans = []
        for key, vals in count.items():
            temp = []
            for val in vals:
                if len(temp) == key:
                    ans.append(temp.copy())
                    temp = []
                temp.append(val)
            if temp: ans.append(temp.copy())

        
        return ans