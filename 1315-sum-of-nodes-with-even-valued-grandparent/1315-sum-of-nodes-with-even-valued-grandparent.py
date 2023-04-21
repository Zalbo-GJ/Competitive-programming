# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        stack = []
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return
            if len(stack) > 1 and stack[-2].val % 2 == 0:
                ans += node.val
            
            stack.append(node)
            dfs(node.left)
            dfs(node.right)
            stack.pop()
            
        dfs(root)
        
        return ans
        