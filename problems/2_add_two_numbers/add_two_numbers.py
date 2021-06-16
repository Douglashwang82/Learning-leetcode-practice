# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = l3 = ListNode()
        ex = 0
        while l1 or l2 or ex:
            temp = ListNode()
            temp.val += ex
            if l1:
                temp.val += l1.val
                l1 = l1.next
            if l2:
                temp.val += l2.val
                l2 = l2.next
            ex, temp.val= divmod(temp.val, 10)
            l3.next = temp
            l3 = l3.next
        return ans.next
        