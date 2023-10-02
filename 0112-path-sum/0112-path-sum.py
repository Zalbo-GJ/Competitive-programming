# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, path_sum):
            if not node.left and not node.right:
                if path_sum == targetSum:
                    return True
                return False
            right = False
            left = False
            if node.left:
                left = dfs(node.left, path_sum + node.left.val)
            if node.right:
                right = dfs(node.right, path_sum + node.right.val)
                
            return left or right
        
        return dfs(root, root.val) if root else False
                