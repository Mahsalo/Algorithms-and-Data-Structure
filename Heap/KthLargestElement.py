
### O(Nlog K) time and O(K) space
### Remove the min element if the next one bigger
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        j = 0
        for i in range(len(nums)):
            if j<k:
                heapq.heappush(pq, nums[i])
                j +=1
            else:
                top = pq[0]
                if nums[i]>top:
                    heapq.heappop(pq) #remove the min element
                    heapq.heappush(pq, nums[i]) #put the new big value in the minHeap
        return pq[0]
                
