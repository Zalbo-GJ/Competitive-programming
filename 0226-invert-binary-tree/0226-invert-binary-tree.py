# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        
        inverted = TreeNode(root.val)
        
        def dfs(node, invert):
            if not node:
                return
            if node.left:
                invert.right = TreeNode(node.left.val)
                dfs(node.left, invert.right)
            if node.right:
                invert.left = TreeNode(node.right.val)
                dfs(node.right, invert.left)

            
        
        dfs(root, inverted)
        
        return inverted