import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #max k = max number in list
        # try different k's, track hours, if we get above h then go onto next k
        # binary search for k
        # if we clear bananas, then k too big, move right to mid - 1
        # if we get to hours = h before clearing, then k too small, move left to mid - 1

        left = 1
        right = max(piles)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            hours = self.eat(piles, h, mid)
            if hours == 1 or hours == 0:
                right = mid - 1
                result = mid
            if hours == -1:
                left = mid + 1
        return result
    
    def eat(self, piles: List[int], h: int, k: int) -> int:
        i = 0
        hours = 0
        for i in range(len(piles)):
            if (piles[i] <= k):
                hours += 1
            else:
                hours += math.ceil(piles[i] / k)
        print (hours)
        if hours < h:
            return 1
        if hours > h:
            return -1
        if hours == h:
            return 0



