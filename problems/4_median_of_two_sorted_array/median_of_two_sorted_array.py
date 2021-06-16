class List(list):
    pass

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        We notice that we are required an O(log(n+m)) algorihtnm.
        This is a big hint.
        Binary search is O(log n).
        Solving process:
            1. we have two sorted arrays. (increasing)
            2. (IMPORTANT) we know the exactly index we want which is [len(n + m) //2].
            3. Handling the odd length or even length.
                - if odd, return founded value
                - if even, return (founded value / the value before founded value) / 2
            4. So, we can assign two pointers pointing the start of the two arrays.
            5. We know exactly how many moves we want to move our pointers because of step 2.
            6. Looping part:
                - Let "before_mid" store the value in "mid". (keep tracking the value before "mid")
                - Comparing nums1[p1] and nums2[p2]. (Handling invalid index error using length checking.)
                - take the small one and store it into mid parameter.
                - move the pointer with smaller value.
        """
        n = len(nums1)
        m = len(nums2)
        target = (n + m) // 2
        mid = before_mid = 0
        p1 = p2 = even = 0
        while target >= 0:
            before_mid = mid
            if p1 < n and p2 < m and nums1[p1] > nums2[p2]:
                mid = nums2[p2]
                p2 += 1
            elif p1 < n and p2 < m and nums1[p1] <= nums2[p2]:
                mid = nums1[p1]
                p1 += 1
            elif p1 < n:
                mid = nums1[p1]
                p1 += 1
            elif p2 < m:
                mid = nums2[p2]
                p2 += 1
            target -= 1
        # Check the final length of the merged list
        # If even, take the mid from index(len(n+m)//2) and the value before it.
        # So, we need to keep tracking the element before current value.
        # If odd, just return the found mid.
        if (n+m) % 2 == 0:
            return (mid + before_mid) / 2
        return mid