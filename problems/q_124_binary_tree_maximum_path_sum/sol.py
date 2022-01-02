# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_maximum = root.val
        
        def postorder(root):
            
            # root check
            if not root:
                return 0
            
            if not root.left and not root.right:
                self.global_maximum = max(self.global_maximum, root.val)
                return root.val
            
            # postorder part
            left = postorder(root.left)
            right = postorder(root.right)
            
            # actions
            local_maximum = max(left + root.val, right + root.val, root.val)
            self.global_maximum = max(self.global_maximum, local_maximum, left + root.val + right)
            return local_maximum
        
        
        postorder(root)
        return self.global_maximum