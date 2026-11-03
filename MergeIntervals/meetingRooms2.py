### Minimum number of meeting rooms needed for different time intervals == maximum number of conflict/overlaps between intervals
### Plot the intervals and keep track of the meetings starts (++) and ends (--)
### If several meetings start at the same time or end at the same time (+K or -K)
### O(NlogN) time and O(N) space

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        begin = {}
        end = {}

        for i in range(len(intervals)):
            if intervals[i].start in begin:
                begin[intervals[i].start] +=1
            else:
                begin[intervals[i].start] =1

            if intervals[i].end in end:
                end[intervals[i].end] +=1
            else:
                end[intervals[i].end] =1

        
        ### Sort both the begin and end 
        begin = {k: begin[k] for k in sorted(begin)}
        end = {k: end[k] for k in sorted(end)}


        count = 0
        maxx = 0

        for i in range(max(end.keys())+1):
            if i in end:
                count = count - end[i]
            if i in begin:
                count = count + begin[i]
            if count > maxx:
                maxx = count
        return maxx
          


            





