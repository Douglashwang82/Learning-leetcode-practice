class MedianFinder:

    def __init__(self):
        self._minheap = []
        self._maxheap = []
        self._minheap_length = 0
        self._maxheap_length = 0
        
    def _upheap_min(self, index):
        """Bubbling down on minheap"""
        parent = (index - 1) // 2
        if index > 0 and self._minheap[parent] > self._minheap[index]:
            self._minheap[parent], self._minheap[index] = self._minheap[index], self._minheap[parent]
            self._upheap_min(parent)
            
    def _downheap_min(self, index):
        """Bubbling down on minheap"""
        left = 2* index + 1
        right = 2*index + 2
        if left < self._minheap_length:
            small = left
            if right < self._minheap_length and self._minheap[left] > self._minheap[right]:
                small = right
            if self._minheap[small] < self._minheap[index]:
                self._minheap[small], self._minheap[index] = self._minheap[index], self._minheap[small]
                self._downheap_min(small)
        
    def _upheap_max(self, index):
        """Bubbling up on maxheap"""
        parent = (index - 1) // 2
        if index > 0 and self._maxheap[parent] < self._maxheap[index]:
            self._maxheap[parent], self._maxheap[index] = self._maxheap[index], self._maxheap[parent]
            self._upheap_max(parent)
            
    def _downheap_max(self, index):
        """Bubbling down on maxheap"""
        left = 2* index + 1
        right = 2*index + 2
        if left < self._maxheap_length:
            large = left
            if right < self._maxheap_length and self._maxheap[left] < self._maxheap[right]:
                large = right
            if self._maxheap[large] > self._maxheap[index]:
                self._maxheap[large], self._maxheap[index] = self._maxheap[index], self._maxheap[large]
                self._downheap_max(large)
                
    def _balance(self):
        """Keep two heaps in balance"""
        if self._maxheap_length < self._minheap_length:
            # extract one from min to max
            self._minheap[0], self._minheap[-1] = self._minheap[-1], self._minheap[0]
            num = self._minheap.pop()
            self._minheap_length -= 1
            self._downheap_min(0)
                
            self._maxheap.append(num)
            self._maxheap_length += 1
            self._upheap_max(self._maxheap_length - 1)
                
        if self._maxheap_length - self._minheap_length > 1:
            # extract one from max to min
            self._maxheap[0], self._maxheap[-1] = self._maxheap[-1], self._maxheap[0]
            num = self._maxheap.pop()
            self._maxheap_length -= 1
            self._downheap_max(0)
            self._minheap.append(num)
            self._minheap_length += 1
            self._upheap_min(self._minheap_length - 1)
        
    def addNum(self, num: int) -> None:
        """Adding new number to heaps"""
        if self._maxheap_length == 0:
            self._maxheap.append(num)
            self._maxheap_length += 1
        else:
            lower = self._maxheap[0]
            if num < lower:
                self._maxheap.append(num)
                self._maxheap_length += 1
                self._upheap_max(self._maxheap_length - 1)
            else:
                self._minheap.append(num)
                self._minheap_length += 1
                self._upheap_min(self._minheap_length - 1)
        self._balance()
        
    def findMedian(self) -> float:
        isOdd = (self._minheap_length + self._maxheap_length) % 2 != 0
        if isOdd:
            return self._maxheap[0]
        else:
            return (self._maxheap[0] + self._minheap[0]) / 2