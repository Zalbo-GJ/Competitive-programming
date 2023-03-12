# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
       
        
        def path(node,curr):
            
            if curr:
                curr += "->" + str(node.val)
            else:
                curr += str(node.val)
            
            if not node.right and not node.left:
                ans.append(curr)
            
            if node.left:
                path(node.left, curr)
            
            if node.right:
                path(node.right, curr)
        
        path(root, "")
            
           
        
        return ans
            
            
            
            
            
            
        