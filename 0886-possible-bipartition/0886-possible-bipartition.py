class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        lookup = defaultdict(list)
        
        for a, b in dislikes:
            lookup[a].append(b)
            lookup[b].append(a)
        
        
        def dfs(person, gr):
            if not group[person]:
                group[person] = gr
            else:
                return group[person] == gr
            
            for p in lookup[person]:
                if not dfs(p, 2 if gr == 1 else 1):
                    return False
            
            return True
        
        group = [0 for _ in range(n + 5)]
        for person in range(1, n + 1):
            if not group[person] and not dfs(person, 1):
                return False
        
        return True