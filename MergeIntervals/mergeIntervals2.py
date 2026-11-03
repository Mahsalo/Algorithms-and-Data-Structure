#### This is a better and a cleaner version of the solution (update the last added element in the list)
#### First we need to sort the intervals (o(nlogn)) then merge if there is an overlap
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]
        

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if res[-1][1] >= intervals[i][0]: #merging needed
                res[-1][1] = max(res[-1][1], intervals[i][1])
                
            else:
                res.append([start, end])
        return res
