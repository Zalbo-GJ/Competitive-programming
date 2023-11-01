# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []

        dummy = TreeNode(0)
        dummy.left = root
        def dfs(node):
            nonlocal ans
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            
            if node.left and node.left.val in to_delete:
                if node.left.left:
                    ans.append(node.left.left)
                if node.left.right:
                    ans.append(node.left.right)
                node.left = None
            if node.right and node.right.val in to_delete:
                if node.right.left:
                    ans.append(node.right.left)
                if node.right.right:
                    ans.append(node.right.right)
                node.right = None

        if root.val not in to_delete:
            ans.append(dummy.left)
        
        dfs(dummy)
        
        return ans
            
            