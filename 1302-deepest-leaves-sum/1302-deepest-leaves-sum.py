# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        que = deque([root])
        while que:
            size = len(que)
            ans = 0
            
            for _ in range(size):
                node = que.popleft()
                ans += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
                
        return ans
                
            
            
            
        