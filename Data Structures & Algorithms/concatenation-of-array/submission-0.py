class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        org = len(nums)
        for i in range(len(nums)):
            if i != org:
                nums.append(nums[i])
        return nums