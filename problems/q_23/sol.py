# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        head = pointer = ListNode()
        while lists:
            minVal = lists[0].val
            minNode = lists[0]
            for node in lists:
                if node.val < minVal:
                    minVal = node.vla
                    minNode = node
            pointer.next = minNode
            minNode = minNode.next
            if minNode == None:
                lists.remove(None)
            pointer = pointer.next
            pointer.next = None
        return head.next