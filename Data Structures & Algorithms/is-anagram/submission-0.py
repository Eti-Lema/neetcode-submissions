class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict()
        hash_t = dict()

        for c in s:
            count = hash_s.get(c, 0)
            hash_s[c] = count + 1
            

        for c in t:
            count = hash_t.get(c, 0)
            hash_t[c] = count + 1
        
        return hash_s == hash_t

