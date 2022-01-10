# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def __init__(self):
        self._aheap = []
        self._aheap_length = 0
        
    def _swap(self, i, j):
        """Swap two element in the heap"""
        self._aheap[i], self._aheap[j] = self._aheap[j], self._aheap[i]

        
    def _up_heap(self, curr):
        """Bubbling up curr -> 0"""
        parent = (curr - 1) // 2
        if curr > 0 and self._aheap[curr][0] < self._aheap[parent][0]:
            self._swap(curr, parent)
            self._up_heap(parent)

    def _down_heap(self, curr):
        """Bubbling down curr -> end"""
        left = 2*curr + 1
        right = 2*curr + 2
        if left < self._aheap_length:
            small = left
            if right < self._aheap_length and self._aheap[right][0] < self._aheap[left][0]:
                small = right
            if self._aheap[curr][0] > self._aheap[small][0]:
                self._swap(small, curr)
                self._down_heap(small)
                
    def _heapify(self):
        """Bottom up approach construct a heap"""
        if self._aheap:
            start = self._aheap_length - 1
            for i in range(start, -1, -1):
                self._down_heap(i)
    
    def _remove_and_push(self):
        """Remove the min value in the heap.
                Swap the first element and the last element
                Pop the last element
                Do downheap(first_index) after pop()
           Push another node into the heap if poped node has .next
                Do upheap(last_index) if adding new element
        """
        self._swap(0, self._aheap_length - 1)
        _, output = self._aheap.pop()
        self._aheap_length -= 1
        self._down_heap(0)
        if output.next:
            self._aheap.append((output.next.val, output.next))
            self._aheap_length += 1
            self._up_heap(self._aheap_length - 1)
        return output
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # initial a dummy node for easy output, tail for easy access to the end
        dummy = tail = ListNode()
        
        # use this to store every "first node" in every lists
        self._aheap = [(li.val, li) for li in lists if li]
        self._aheap_length = len(self._aheap)
        
        # build an actual minheap
        self._heapify()
        
        # linking the node by constantly remove_and_push() from the heap
        while self._aheap:    
            tail.next = self._remove_and_push()
            tail = tail.next
        
        return dummy.next