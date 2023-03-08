# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        ans = []
        
        que = collections.deque()
        que.append(root)
        
        while que:
            q = len(que)
            level = []
            for _ in range(q):
                
                node = que.popleft()
                
                if node:
                    level.append(node.val)
                    
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)

            if level:
                ans.append(level)
                
        
        return ans
        
        
            
            
        
        
       
            
            
                    