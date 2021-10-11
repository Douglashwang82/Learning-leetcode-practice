"""
    Working pieces:
        1. Linked list operation
    Direction:
        1. pointer operation
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = mid = right = head    #left: node before target, mid:target node, right: tail
        counter = n
        while right.next != None:
            right = right.next
            counter -= 1
            if counter <= 0:
                mid = mid.next
            if counter < 0:    # left pointer one step behind mid pointer
                left = left.next

        if mid == head:        # remove the head
            return mid.next
        else:
            left.next = mid.next # remove the target element not head.
            return head

