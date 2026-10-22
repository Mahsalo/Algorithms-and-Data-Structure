# Container area is determined by the lowest height of the bars

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        max = 0
        while p1<p2:
            if heights[p1] < heights[p2]:
                h = heights[p1]
                w = p2 - p1 #always positive
                p1 +=1
            else:
                h = heights[p2]
                w = p2 - p1 #always positive
                p2 -=1
    
            
            area = h*w #always positve

            if area>max:
                max = area
        return max
