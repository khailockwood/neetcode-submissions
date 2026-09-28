class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #merge until start of next interval greater than end of current interval
        intervals.sort(key = lambda x: x[0])

        merged = []
        merged.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[len(merged) - 1][1] and intervals[i][1] >= merged[len(merged) - 1][1]:
                merged[len(merged) - 1][1] = max(intervals[i][1], merged[len(merged) - 1][1])
            elif intervals[i][1] >= merged[len(merged) - 1][1]:
                merged.append(intervals[i])
    
        return(merged)