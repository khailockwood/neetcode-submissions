class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for i in range(len(nums)): #loop through each number in nums
            for j in range(len(subs)): #looping throguh every existing subarray in subs
                subs.append(subs[j] + [nums[i]]) #append to subs the subarray we're looking at plus the next num value (tracked by [i])
        return subs