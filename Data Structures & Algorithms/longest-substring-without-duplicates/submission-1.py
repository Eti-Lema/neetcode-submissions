class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        max_len = 0
        right = 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left +=1
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len