class Solution:
    def rob(self, nums: List[int]) -> int:
        #maxNum = 0
        cache = {}

        def findMax(index, cache):
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]

            cache[index] = max(nums[index] + findMax(index + 2, cache), findMax(index + 1, cache))

            return cache[index]
        
        #res = findMax(0, cache)
        #if res > maxNum:
            #maxNum = res

        return findMax(0, cache)