class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i in range(len(nums)):
            complement = target - nums[i]
            if hashmap.get(complement) is not None:
                return [hashmap.get(complement), i]
            hashmap[nums[i]] = i
        
        return []