import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heap, pop out of heap if len(heap) > k
        # store the frequency of every element, heap of mapped values
        # map each number to it's frequency as we iterate

        hashMap = {}
        heap = []

        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        
        for num in hashMap.keys():
            heapq.heappush(heap, (hashMap[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        print(heap)
        res = []
        for j in range(k):
            res.append(heapq.heappop(heap)[1])
        print(res)
        return res
