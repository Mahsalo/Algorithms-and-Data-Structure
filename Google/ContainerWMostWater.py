#### Use two pointers approach to decrease time complexity from O(N^2) to O(N)
#### Left pointer and right pointer to both sides of the array, move the pointer with the smaller (or equal) height to the inward direction 
#### Continue until the width becomes zero!

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_area = 0
        i=0 # left pointer
        j=len(height)-1 # right pointer
        W = j-i #width, continue until the width is zero ---> <---
        
        while (W>0):

            if height[j] >= height[i]:
                area = height[i]*W
                i +=1
            else: 
                area = height[j]*W
                j -=1
            
            if area>max_area:
                max_area = area

            W = j-i
        return max_area
