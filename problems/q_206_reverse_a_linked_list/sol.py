# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newhead = head
        head = head.next
        newhead.next = None
        
        while head:
            temp = head
            head = head.next
            temp.next = newhead
            newhead = temp
        
        return newhead