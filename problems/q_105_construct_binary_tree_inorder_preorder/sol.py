# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildSubTree(pre_s, pre_e, in_s, in_e):
            parent = None
            
            if pre_s < pre_e:
                parent = TreeNode(preorder[pre_s])
                diff = in_dict[preorder[pre_s]] - in_s
                parent.left = buildSubTree(pre_s + 1, pre_s + diff, in_s, in_s + diff)
                parent.right = buildSubTree(pre_s + diff + 1, pre_e, in_s + diff + 1, in_e)   
            
            # Reach leafs
            elif pre_s == pre_e:
                parent = TreeNode(preorder[pre_s])
                
            return parent


        # Performance boost. The tree only conains unique value! -> Dict/Set (hash table) -> O(1) searching
        pre_dict = {k:i for i,k in enumerate(preorder)}
        in_dict = {k:i for i,k in enumerate(inorder)}
        length = len(preorder) - 1
        return buildSubTree(0, length, 0, length)