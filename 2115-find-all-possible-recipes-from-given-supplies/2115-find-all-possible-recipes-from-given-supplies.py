class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:

                graph[ingredient].append(recipes[i])
                if not indegree[recipes[i]]:
                    indegree[recipes[i]] = 1
                else:
                    indegree[recipes[i]] += 1

        que = deque(supplies)

        while que:

            ingredient = que.popleft()
            
            if ingredient in recipes:
                ans.append(ingredient)

            for ing in graph[ingredient]:
                indegree[ing] -= 1
                if indegree[ing] == 0:
                    que.append(ing)
            
        return ans
                
            
            