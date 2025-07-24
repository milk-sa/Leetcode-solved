class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        modified_nums = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        left = 0
        right = len(nums)-1     
        for i in range(len(nums)):
            if nums[i] != 0:
                modified_nums.append(nums[i])   
        while len(modified_nums) < len(nums):
            modified_nums.append(0)

        return modified_nums         