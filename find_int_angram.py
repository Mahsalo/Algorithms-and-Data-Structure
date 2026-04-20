from collections import defaultdict
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(list)
        a = []
        for idx, j in enumerate(nums2):
            d[j].append(idx)

        for i in nums1:
            a.append(d[i].pop())
            
        return a
