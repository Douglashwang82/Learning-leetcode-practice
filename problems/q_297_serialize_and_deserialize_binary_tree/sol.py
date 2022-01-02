# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        element_list = []
        bqueue = queue.Queue()
        if root:
            bqueue.put((root, 0))
        while not bqueue.empty():
            temp, position = bqueue.get()
            left_position = (2*position) + 1
            right_position = (2*position) + 2
            value = temp.val
            prepare = str(position)+ "*"+ str(value)
            if temp.left:
                bqueue.put((temp.left, left_position))
            if temp.right:
                bqueue.put((temp.right, right_position))
            element_list.append("x" + prepare + "x")
        code = "".join(element_list)
        return code
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        setDict = {}
        decode1 = data.split("x")
        decode2  = [c.split("*") for c in decode1 if c]
        for e in decode2:
            setDict[int(e[0])] = TreeNode(e[1])
        for e in decode2:
            curr_position = int(e[0])
            left_position = 2*curr_position + 1
            right_position = 2*curr_position + 2
            if setDict.get(left_position):
                setDict[curr_position].left = setDict[left_position]
            if setDict.get(right_position):
                setDict[curr_position].right = setDict[right_position]
        return setDict[0]
        
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))