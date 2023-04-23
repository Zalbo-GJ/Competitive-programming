# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = root.val
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            leftMx = dfs(node.left) 
            rightMx = dfs(node.right)
            leftMx = max(leftMx, 0)       
            rightMx = max(rightMx, 0)
            
            ans = max(ans, node.val + leftMx + rightMx)
            
            return node.val + max(leftMx, rightMx)
        
        dfs(root)
        
        return ans