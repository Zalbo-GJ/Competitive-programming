# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj = defaultdict(list)
        def dfs(node, par):
            if not node:
                return 
            
            if par != -1:
                adj[node.val].append(par.val)
                
            if node.left:
                adj[node.val].append(node.left.val)
                dfs(node.left, node)
            if node.right:
                adj[node.val].append(node.right.val)
                dfs(node.right, node)
        
        dfs(root, -1)
        visited = {target.val}
        ans = []
        que = deque([[target.val, 0]])
        while que:
            for _ in range(len(que)):
                node, dist = que.popleft()
                if dist == k:
                    ans.append(node)
                    continue
                
                for val in adj[node]:
                    
                    if val not in visited:
                        que.append([val, dist + 1])
                        visited.add(val)
        
        return ans