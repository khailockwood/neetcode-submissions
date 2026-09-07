class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(startIndex, currSum, currCombination) -> List[List[int]]:
            if currSum == target: #found a subset equal to target, pass to results and reset parameters
                results.append(currCombination.copy())
                currCombination = []
                currSum = 0
                return
            if currSum > target:
                return
            if startIndex >= len(nums):
                return
            currSum += nums[startIndex]
            currCombination.append(nums[startIndex])
            backtrack(startIndex, currSum, currCombination) # find every subset starting with this startIndex
            currCombination.pop() #have looked at every subset starting with previous startIndex, now pop it out, move on to next startIndex, start now from there
            currSum -= nums[startIndex] #have to remove the previous startIndex from sum, it's no longer being included in subsets
            backtrack(startIndex + 1, currSum, currCombination) #startIndex + 1 moves to next startIndex, starts process over again.



        backtrack(0, 0, [])
        return results
