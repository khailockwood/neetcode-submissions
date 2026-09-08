class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)

        while(len(maxHeap) > 1):
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, x-y)
        
        if len(maxHeap) == 1:
            return abs(heapq.heappop(maxHeap))
        else:
            return 0
            
        