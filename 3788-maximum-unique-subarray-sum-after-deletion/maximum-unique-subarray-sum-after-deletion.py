class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = {}
        nums.sort()
        max_sum = nums[len(nums)-1]
        dic[nums[len(nums)-1]] = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in dic:
                continue
            else:
                
                max_sum = max(max_sum+nums[i],max_sum)
                dic[nums[i]] = i
        if len(nums) == 1:
            max_sum = nums[0]       
        return max_sum            
        