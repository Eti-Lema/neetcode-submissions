class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        product = 1
        for j in range(len(ans) - 1, -1, -1):
            ans[j] = ans[j] * product
            product = product * nums[j]
            
        
        return ans
        
        