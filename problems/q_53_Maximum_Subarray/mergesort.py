def merge_sort(nums):
    nums_length = len(nums)
    if nums_length < 2: return nums                         # Stop point
    mid = nums_length // 2                                  
    left_side = merge_sort(nums[:mid])                      # Divide into two subarrays
    right_side = merge_sort(nums[mid:])
    return merge(left_side, right_side)                     # Return the merged array

def merge(nums1, nums2):
    result = []                                             # addtion spaces to store a ordered array
    i = j = 0                                               # pointers for nums1 and nums2
    nums1_length = len(nums1)
    nums2_length = len(nums2)
    while i < nums1_length and j < nums2_length:            # Comparing two array's first element
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    result = result + nums1 if i < nums1_length else result # adding the remaining subarray into result[] either nums1 or nums2
    result = result + nums2 if j < nums2_length else result
    return result
            


target = [1,3,2]
print(merge_sort(target))