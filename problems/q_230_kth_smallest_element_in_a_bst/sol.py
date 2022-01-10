class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, k):
            if root:
                for p in inorder_subtree(root):
                    if k == 1:
                        return p.val
                    k -= 1
                
        def inorder_subtree(root):
            if root:
                for other in inorder_subtree(root.left):
                    yield other
                yield root
                for other in inorder_subtree(root.right):
                    yield other
                    
        return inorder(root, k)