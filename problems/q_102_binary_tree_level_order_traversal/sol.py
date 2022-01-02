# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfsQueue = queue.Queue()
        a_dict = {}
        if root:
            bfsQueue.put((root, 0))
        while not bfsQueue.empty():
            temp_node, temp_level = bfsQueue.get()
            if a_dict.get(temp_level):
                a_dict[temp_level] += [temp_node.val]
            else:
                a_dict[temp_level] = [temp_node.val]
            if temp_node.left:
                bfsQueue.put((temp_node.left , temp_level + 1))
            if temp_node.right:
                bfsQueue.put((temp_node.right, temp_level + 1))
        
        res = [a_dict[k] for k in a_dict]
        
        return res