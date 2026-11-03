### Insert a new interval into the list of the intervals and make sure the final result is still sorted (merge if needed)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        ### Sort it
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append([start, end])
        return res
