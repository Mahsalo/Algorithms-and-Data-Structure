class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        l.sort()

        start = l[0][0]
        end = l[0][1]
        res = []

        for i in range(1, len(l)):
            if l[i][0] <= end:
                # Overlap: extend the current interval
                end = max(end, l[i][1])
            else:
                # No overlap: save the current interval
                res.append([start, end])

                # Start a new interval
                start = l[i][0]
                end = l[i][1]

        # Append the last interval
        res.append([start, end])

        return res
