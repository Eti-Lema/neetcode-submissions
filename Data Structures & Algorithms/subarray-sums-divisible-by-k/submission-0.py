class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num
            remainder = prefix % k
            count += freq.get(remainder, 0)
            freq[remainder] = freq.get(remainder, 0) + 1
        
        return count