# https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorder(root, lower, upper):
            if not root:
                return True
            if lower >= root.val or root.val >= upper:
                return False
            return preorder(root.left, lower, root.val) and preorder(root.right, root.val, upper)
        return preorder(root, float(-inf), float(inf))