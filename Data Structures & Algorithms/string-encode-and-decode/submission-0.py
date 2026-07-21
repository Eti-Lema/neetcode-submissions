class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        ans = ""
        for word in strs:
            ans += str(len(word)) + delimiter + word
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length

            ans.append(s[word_start:word_end])

            i = word_end

        return ans


