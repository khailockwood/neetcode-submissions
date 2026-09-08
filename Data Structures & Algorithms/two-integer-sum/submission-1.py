class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution
        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    result.append(i)
                    result.append(j)
        return result
