import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        while (len(maxHeap) > 1):
            copyHeap = maxHeap.copy()
            x = heapq.heappop(copyHeap)
            y = heapq.heappop(copyHeap)
            if x == y:
                heapq.heappop(maxHeap)
                heapq.heappop(maxHeap)
            if x < y:
                heapq.heappop(maxHeap)
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, x-y)
        
        if len(maxHeap) == 1:
            return abs(heapq.heappop(maxHeap))
        else:
            return 0



        