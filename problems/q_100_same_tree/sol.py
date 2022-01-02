# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
from typing import Sequence
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            queueBFS = queue.Queue()
            if root:
                queueBFS.put(root)
            while not queueBFS.empty():
                temp = queueBFS.get()
                if temp == "null":
                    yield None
                    continue
                yield temp
                if temp.left:
                    queueBFS.put(temp.left)
                else:
                    queueBFS.put("null")
                if temp.right:
                    queueBFS.put(temp.right)
                else:
                    queueBFS.put("null")
        
        se1 = [e.val if e else "null" for e in bfs(p)]
        se2 = [e.val if e else "null" for e in bfs(q)]

        return se1 == se2



