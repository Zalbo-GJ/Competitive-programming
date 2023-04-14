"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        depth = 0
        def dfs(node, level):
            nonlocal depth
            if not node.children:
                depth = max(depth,level)
                return 
            
            level += 1
            for child in node.children:
                dfs(child,level)
            
            
        dfs(root,1)
        return depth
        