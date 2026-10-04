class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        def recurse(currSum):
            minCoins = float('inf')
            if currSum == 0:
                return 0

            if currSum < 0:
                return float('inf')

            if currSum in cache:
                return cache[currSum]

            for coin in coins:
                if coin <= currSum:
                    cache[currSum] = minCoins = min(minCoins, 1 + recurse(currSum - coin))

            return minCoins
                

        result = recurse(amount)
        if result == float('inf'):
            return -1
        else:
            return result
            

            
            
