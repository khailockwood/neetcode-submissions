class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at each index, find the mine of the everything before it
        currMin = prices[0]
        maxDiff = 0
        for i in range(len(prices) - 1):
            if prices[i] < currMin:
                currMin = prices[i]
            if (prices[i + 1] - currMin) > maxDiff:
                maxDiff = (prices[i + 1] - currMin)

        return maxDiff