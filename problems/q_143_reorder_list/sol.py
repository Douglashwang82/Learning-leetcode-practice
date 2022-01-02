# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        aList = []
        cursor = head
        while cursor:
            aList.append(cursor)
            cursor = cursor.next
        
        left = 0
        right = len(aList) - 1
        while left <= right - left:
            aList[left].next = aList[right]
            left += 1
            aList[right].next = aList[left]
            right -= 1
        
        aList[left].next = None