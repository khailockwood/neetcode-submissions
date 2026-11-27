class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #loop through existing subsets, adding the new num to each subset, then add that new subset,
        #need to be able to check for duplicates: sort array, if nums[i] != nums[i-1], can add nums[i] to every subset, if nums[i] == nums[i-1], only add nums[i] to subsets that were just appended by duplicate num
        #works because: when sorted, a num will have just been appended to all subsets, seeing a duplicate of that num, if we do that same appending to all we duplicate the work just done and create duplicates, only want to add to those that already have the previous number
        '''example: [1, 2, 1]:
            - [], then add 1 to [], add [1]
            - look at 2, add 2 to [], append [2], add 2 to [1], add [1,2]
            - look at 1, add 1 to [], see dup, don't add, add 1 to [1], append [1,1], add 1 to [1,2], append [1,2,1]

        '''
        results = [[]]

        numsSorted = sorted(nums)
        prevEnd = 0 #where the previous iteration started appending is the size of the list before appending in that interation
        #start the next iteration wherever the previous iteration started appending (prevEnd)

        for i in range(len(numsSorted)):
            start = 0
            if i > 0 and numsSorted[i] == numsSorted[i-1]:
                start = prevEnd
            prevEnd = len(results)
            for j in range(start, len(results)):
                results.append(results[j] + [numsSorted[i]])


        return results
            
