class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            front = self.find_the_position_to_switch(nums)
            if front != None:  # if None, it means the list is in decending order.
                back = self.find_the_least_position_to_switch(nums, nums[front])
                self.switch_two_item(front, back, nums)
                self.my_selection_sort(nums,front + 1)
            else:
                self.my_selection_sort(nums, 0) # the list is in descending order,
                                                # just sort it in ascending order.
                    
    def find_the_position_to_switch(self, nums):
        for i in range(len(nums) - 1, 0 , -1):
            if nums[i] > nums[i - 1]:
                return i - 1
    
    def find_the_least_position_to_switch(self,nums,flag):
        for i in range(len(nums) - 1, 0, - 1):
            if nums[i] > flag:
                return i
    
    def switch_two_item(self,front,back,nums):
        nums[front],nums[back] = nums[back],nums[front]
    
    def my_selection_sort(self, nums, flag):
        for i in range(flag, len(nums)):
            minimum = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                   minimum = j
            nums[i],nums[minimum] = nums[minimum],nums[i]