class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans


    def backtrack(self, nums: List[int], path: List[int], ans: List[List[int]]) -> None:
        if len(nums) == len(path):
            ans.append(path.copy())
            return
        for num in nums:
            if num in path:
                continue
            path.append(num)
            self.backtrack(nums, path, ans)
            path.pop()
