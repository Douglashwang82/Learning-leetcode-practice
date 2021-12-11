class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pmin = pmax = 1
        gmax = nums[0]
        for num in nums:
            tpmin = pmin
            pmin = min(num, pmin* num, pmax *num)
            pmax = max(num, tpmin*num , pmax *num)
            gmax = max(gmax, pmax)
        return gmax