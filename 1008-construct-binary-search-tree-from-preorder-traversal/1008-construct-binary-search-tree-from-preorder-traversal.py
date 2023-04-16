# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(preorder[0])
        stack = [root]
      
        for ind in range(1, len(preorder)):

            if preorder[ind] < stack[-1].val:
                stack[-1].left = TreeNode(preorder[ind])
                stack.append(stack[-1].left)
            else:
                
                while stack and stack[-1].val < preorder[ind]:
                    last = stack.pop()
                

                last.right = TreeNode(preorder[ind])
                stack.append(last.right)
    
        return root


       
        