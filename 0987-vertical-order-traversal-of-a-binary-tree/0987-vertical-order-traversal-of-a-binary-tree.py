# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        columns = defaultdict(list) 
        
        def traverse(root, row, col):
            nonlocal columns
            
            if not root:
                return
            
            columns[col].append([row, root.val])
            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)
            
            
        traverse(root, 0, 0)
                 
        output = []
        for key in sorted(columns):
            columns[key].sort()
            
            temp = []
            for i, j in columns[key]:
                temp.append(j)
                
            output.append(temp)
        
        return output