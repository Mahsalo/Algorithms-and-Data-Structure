### Pivot is the idx at which summ of elements in the right (excluding pivot) == sum of elements in the left (excluding pivot)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = dict()
        pref[0] = nums[0]

        # Make the prefix sum array
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i]

        # Find th epivot point using the magic formula: remember the formula includes the last element but pivot must be excluded
        if pref[len(nums)-1] - pref[0] ==0: # from index 1 to the end
            return 0 # index 0 is the pivot
        
        for idx in range(1, len(nums)):
            left_sum = pref[idx-1] #since we always start from iindex =0 to get the sum
            right_sum = pref[len(nums)-1] - pref[idx]
            if left_sum == right_sum:
                return idx

        return -1
