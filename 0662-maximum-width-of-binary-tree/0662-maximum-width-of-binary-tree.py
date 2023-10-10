# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def bfs():
            que = deque([(0, root)])
            ans = 1
            while que:
                l = len(que)
                for _ in range(l):
                    idx, node = que.popleft()
                    if node.left:
                        que.append([(idx * 2) + 1, node.left])
                    if node.right:
                        que.append([(idx * 2) + 2, node.right])
                
                
                if que:
                    ans = max(ans, que[-1][0] - que[0][0] + 1)
                
            return ans
            
        return bfs()
           
                
                