class Solution:
    def remove_min(self, aheap):
        aheap[0], aheap[-1] = aheap[-1], aheap[0]
        _,output = aheap.pop()
        self.downheap(0, aheap)
        return output
    
    def downheap(self, index ,aheap):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(aheap):
            small = left
            if right < len(aheap) and aheap[left][0] < aheap[right][0]:
                small = right
            if aheap[small][0] > aheap[index][0]:
                aheap[small], aheap[index] = aheap[index], aheap[small]
                self.downheap(small, aheap)

    def heapify(self, alist):
        if alist:
            start = len(alist) - 1
            for i in range(start, -1, -1):
                self.downheap(i, alist)
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # First Part: How to count frequency?
        # Use Hash map to count frequencies in O(n)
        results = []
        hashmap = {key: 0 for key in nums}
        for n in nums:
            hashmap[n] += 1
        alist = [(hashmap[k], k) for k in hashmap.keys()]
        
        
        # Second Part: How to get top k elements?
        # Construct a maxheap by element's frequency
        # Use Heap to extract Top k frequent elements
        self.heapify(alist)
        
        for _ in range(k):
            results.append(self.remove_min(alist))
            
        return results