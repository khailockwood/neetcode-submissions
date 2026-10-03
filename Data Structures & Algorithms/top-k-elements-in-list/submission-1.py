import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        heap = []

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        
        for key in frequencies.keys():
            heapq.heappush(heap, (frequencies[key], key)) #putting a tuple of (num: frequency) in heap

            if len(heap) > k:
                heapq.heappop(heap) #will remove smallest element (num: frequency pair) in heap

        res = []
        for num in heap:
            res.append(num[1])

        return res