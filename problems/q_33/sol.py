"""
    Working Pieces:
        1. ordered but rotated array.
        2. unknown pivot position 
    Directions:
        1. binary search left, right, mid
        2. cases study
"""
class Solution:
        def search(self, nums, target) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target: return mid                      # match
                if nums[left] <= nums[mid]:                             # m1
                    if target >= nums[left] and target < nums[mid]:     # t1
                        right = mid - 1
                    else:                                               # t2
                        left = mid + 1                                  
                elif nums[left] >= nums[mid]: # m2                      # m2
                    if target > nums[mid] and target <= nums[right]:    # t4
                        left = mid + 1
                    else:                                               # t3
                        right = mid - 1
            return -1                                                   # not found

