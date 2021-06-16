class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Concepts:
            Greedy algorithm.
            Two pointer approach.
        
        Solving Process:
            1. First, Try a O(n^2) approach which is computing every amount of in the list. Not efficiency.
            2. Second, Try a greedy algorithm which is using two pointer pointed to the head and tail.
            3.         then moving two pointers untail they meet.
                       Each step should move the pointer with smaller value.
                       (if we move the bigger one, it will always get a lower amount.)
            4. Store and return the maximum value.
        """
        maximum = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            maximum = max(maximum, min(height[left],height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum