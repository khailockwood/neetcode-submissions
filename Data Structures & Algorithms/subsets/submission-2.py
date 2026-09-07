class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for i in range(len(nums)):
            for j in range(len(subs)):
                subs.append(subs[j] + [nums[i]])
        return subs