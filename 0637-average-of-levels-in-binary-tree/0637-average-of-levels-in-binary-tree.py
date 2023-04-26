# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        que = deque()
        que.append(root)
        ans = []
        while que:
            
            total = 0
            currLen = len(que)
            for _ in range(currLen):
                
                node = que.popleft()
                total += node.val     

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(total/currLen)

        return ans