class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for i in range(len(nums)):
            print(nums[i])
            for j in range(len(subs)):
                print(subs[j])
                subs.append(subs[j] + [nums[i]])
        return subs