# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, list1, list2):
        newHead = newTail = ListNode()
        
        while list1 and list2:
            if list1.val >= list2.val:
                newTail.next = list2
                list2 = list2.next
                newTail = newTail.next
            else:
                newTail.next = list1
                list1 = list1.next
                newTail = newTail.next
        newTail.next = list1 or list2
        return newHead.next
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0:
            return 
        if length == 1:
            return lists[0]
        if length == 2:
            return self.merge2Lists(lists[0], lists[1])
        mid = (length - 1) // 2
        
        return self.merge2Lists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))