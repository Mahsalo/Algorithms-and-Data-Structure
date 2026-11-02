#### Continuous subarray sum: If there is a good subarray return true
#### Given a k number, a good subarray has a sum multiple of k (sum%6 =0) and length is more than 2
#### Solution: keep a hashmap of the Remainder (%k) and the index of the prefix, if there is a duplicate in the keys it means we had a good sub-array in between.
#### Map each remainder to the end index



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = dict()
        rem[0] = -1
        pref = 0

        for end in range(len(nums)):
            pref = pref + nums[end]
            r = pref%k
            if r not in rem:
                rem[r] = end
            else:
                if end - rem[r] > 1: # len > 2
                    return True

        return False




