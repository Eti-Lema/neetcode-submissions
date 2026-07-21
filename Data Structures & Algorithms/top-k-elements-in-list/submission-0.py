class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict() #num -> occurences

        for num in nums:
            count = hashmap.get(num, 0)
            hashmap[num] = count + 1
        
        heap = []

        for num, freq in hashmap.items():
            heapq.heappush(heap, (-freq, num))
        
        ans = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            ans.append(num)
        
        
        return ans