class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(startIndex, currSum, currCombination) -> List[List[int]]:
            if currSum == target:
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
            backtrack(startIndex, currSum, currCombination)
            currCombination.pop()
            currSum -= nums[startIndex]
            backtrack(startIndex + 1, currSum, currCombination)



        backtrack(0, 0, [])
        return results
