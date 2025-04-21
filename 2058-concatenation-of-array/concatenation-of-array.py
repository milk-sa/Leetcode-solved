class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      ans = []
      j=0
      for i in range(2*len(nums)):
        if j==len(nums):
            j=0
        ans.append(nums[j])
        j+=1 
        
      return ans      


        