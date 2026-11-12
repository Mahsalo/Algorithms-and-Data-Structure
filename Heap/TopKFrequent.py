#### Time O(nlogk) and space O(n+k)
#### MinHeap sees the first elemnt of a tuple first (and only if similar compares the next elements)

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = dict()
        ### Make a hashmap
        for i in nums:
            if i in h:
                h[i] +=1
            else:
                h[i] = 1

        ### Now solve kth largest element in the array or dict
        pq = []
        j = 0
        ky = list(h.keys())
  
        while j<k:
            heapq.heappush(pq, (h[ky[j]], ky[j]))
            j +=1

        for i in range(j, len(h)):
            if pq[0][0] < h[ky[i]]:
                heapq.heappop(pq)
                heapq.heappush(pq, (h[ky[i]], ky[i]))
       

        return [num for freq, num in pq]
            
        
