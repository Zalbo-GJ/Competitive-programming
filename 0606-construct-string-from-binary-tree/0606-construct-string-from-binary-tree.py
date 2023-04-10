# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(curr):
            s = []
            if not curr:
                return 
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left:
                s.append("("+ str(left)+")")
            elif right:
                s += "()"
            
            if right:
                s.append("("+ str(right)+")")
            
            return str(curr.val) + "".join(s)
        
        
        return dfs(root)
            