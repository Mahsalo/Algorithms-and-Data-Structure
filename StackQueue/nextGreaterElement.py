### Next greater element: use stack otherwise O(n2) in this case O(n+m), only append the stack with the elemnt of n2 if it exists in n1

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        r = dict() 
        res = []


        for i in nums2:
            while s and i>s[-1]:
                last = s.pop()
                r[last] = i
            if i in nums1:
                s.append(i)
            
        for i in nums1:
            if i not in r:
                res.append(-1)
            else:
                res.append(r[i])
        return res
