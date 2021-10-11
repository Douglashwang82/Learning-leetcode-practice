"""
    Working Pieces:
        1. finding element -> bars
        2. left bar and right bar
    Direction:
        1. pointers
        2. for each height, its possible amount is depends on its left bar and right bar.
    
"""

class Solution:
    def trap(self, height) -> int:
        count = 0
        left = [height[0]]
        right = [height[-1]]
        left_counter = height[0]
        right_counter = height[-1]
        for i in range(1, len(height)):
            left_counter = height[i - 1] if left_counter < height[i - 1] else left_counter
            left.append(left_counter)
        for i in range(len(height) - 2, -1, -1):
            right_counter = height[i + 1] if right_counter < height[i + 1] else right_counter
            right.insert(0,right_counter)
        for i in range (1, len(height)):
            bar = min(left[i], right[i])
            amount = bar - height[i]
            if amount > 0:
                count += amount
        return count



s = Solution()
example = [0,1,0,2,1,0,1,3,2,1,2,1]
print('count',s.trap(example))