class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict() # sorted string -> array of the og strings

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = [string]
            else:
                hashmap[sorted_string].append(string)
        
        return list(hashmap.values())