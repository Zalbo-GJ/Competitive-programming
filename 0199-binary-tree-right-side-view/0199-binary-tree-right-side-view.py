# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        def view(node,row):
            
            if not node:
                return
            
            if row >= len(ans): 
                ans.append(node.val)
            
            view(node.right,row + 1)
            view(node.left, row + 1)
            
            
        
        view(root,0)
        
        return ans
        