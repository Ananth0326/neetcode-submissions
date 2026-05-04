class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LEFT = [1] * len(nums)
        for i in range(1, len(nums)):
          LEFT[i] = LEFT[i-1] * nums[i-1]  
        RIGHT = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
           RIGHT[i] = RIGHT[i+1] * nums[i+1]
        output = []
        for i in range(len(nums)):
         output.append(LEFT[i] * RIGHT[i])
        return output