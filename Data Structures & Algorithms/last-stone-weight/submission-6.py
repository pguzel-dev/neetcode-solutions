class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, -abs(x-y))
        
        if len(maxHeap) == 0:
            return 0
        elif len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)
        else:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
        
        return abs(x-y)