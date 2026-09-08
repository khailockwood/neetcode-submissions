import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heapify(self.nums)
        #now have tree heap structure, discard all elements until we have k elements left in heap, then do .heappop
        i = 0
        copy = self.nums.copy()
        while i < (len(self.nums) - self.k):
            heapq.heappop(copy)
            i += 1
        return heapq.heappop(copy)
