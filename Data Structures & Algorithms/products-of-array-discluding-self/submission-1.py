class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        l, r = 1, len(nums) - 2

        while l < len(nums):
            prefix[l] = prefix[l-1] * nums[l - 1]
            suffix[r] = suffix[r+1] * nums[r + 1]

            l += 1
            r -= 1
        
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
        
        return nums
        
