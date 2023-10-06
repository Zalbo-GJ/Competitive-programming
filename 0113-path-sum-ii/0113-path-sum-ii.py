# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        if not root:
            return []
        temp = [root.val]
        def dfs(node, path_sum):
            nonlocal ans, temp
            if path_sum == targetSum and not node.left and not node.right:
                ans.append(temp.copy())
                return
            if node.left:
                temp.append(node.left.val)
                dfs(node.left, path_sum + node.left.val)
                temp.pop()
            if node.right:
                temp.append(node.right.val)
                dfs(node.right, path_sum + node.right.val)
                temp.pop()
            
        
        dfs(root, root.val)
        
        return ans