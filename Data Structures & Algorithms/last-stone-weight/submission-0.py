class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x < y:
                heapq.heappush(heap, -y - (-x))
            elif x == y:
                continue
        
        if len(heap) != 0:
            return -heap[0]
        else:
            return 0
        
