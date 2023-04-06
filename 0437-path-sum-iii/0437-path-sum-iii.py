# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ans = 0
        path =[]
        
        def reverseSum(arr):
            nonlocal targetSum, ans
            tot = 0
            for num in arr[::-1]:
                tot += num
                if tot == targetSum:
                    ans += 1
                
        
        def backtrack(node):
            nonlocal path
            if not node:
                return
            
            path.append(node.val)
            reverseSum(path)
            backtrack(node.left)
            
            backtrack(node.right)
            path.pop()
            
        backtrack(root)
        
        return ans
            
            
            
            
            