import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        #copyHeap = maxHeap.copy()
        while (len(maxHeap) > 1):
            print(maxHeap)
            copyHeap = maxHeap.copy()
            x = heapq.heappop(copyHeap)
            y = heapq.heappop(copyHeap)
            if x == y:
                print(str(x) + " = " + str(y) + "getting rid of both")
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



        