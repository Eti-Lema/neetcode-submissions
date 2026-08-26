class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ans = []
        current = []
        self.backtrack(0, nums, current, ans)
        return ans

    def backtrack(self, i: int, nums: List[int], current: List[int], ans: List[List[int]]):
        if i == len(nums):
            ans.append(list(current))
            return 
        current.append(nums[i])
        self.backtrack(i+1, nums, current, ans)

        current.pop()
        self.backtrack(i+1, nums, current, ans)