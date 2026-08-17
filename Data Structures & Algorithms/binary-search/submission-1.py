class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # We need to look in left half, so right need to be smaller than mid
                r = mid - 1
            else: # We need to look in the right half, so left needs to be bigger than mid
                l = mid + 1
        
        return -1
        