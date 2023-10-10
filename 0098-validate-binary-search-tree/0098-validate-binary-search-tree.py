# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):
            if not node.right and not node.left:
                return [node.val, node.val]
            
            if node.left:
                left = dfs(node.left)
                if not left or left[1] >= node.val:
                    return False
            if node.right:
                right = dfs(node.right)
                if not right or right[0] <= node.val:
                    return False
 
            if node.right and node.left:
                if left[1] >= right[0]:
                    return False
                
                return [min(node.val, left[0]),max(node.val, right[1])]
            elif node.right:
                return [min(node.val, right[0]),max(node.val, right[1])]
            else:
                return [min(node.val, left[0]),max(node.val, left[1])]
            
        ret = dfs(root)
        
        return True if ret else False
                
            
            
                    