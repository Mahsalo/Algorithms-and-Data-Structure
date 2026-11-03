"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: #if no meetings at all, he's free
            return True
        intervals.sort(key=lambda i: i.start) # sort first
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end

            if res[-1].end > intervals[i].start: #conflict
                return False
            else:
                x = Interval(start, end)
                res.append(x)
        return True
