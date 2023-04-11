# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        temp = []
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            
            temp.append(str(node.val))
            
            if not node.left and not node.right:
                ans += int("".join(temp))

            
            dfs(node.left)
            dfs(node.right)
            temp.pop()
        
        dfs(root)
        
        return ans