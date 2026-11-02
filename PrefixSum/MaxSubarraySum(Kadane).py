### Solved maximum subarray sum problem using Kadane's algo. not prefix sum
### Remember it this way
### 1. end always moves forward.
### 2. Keep adding elements while the sum is beneficial.
### 3. If the sum becomes negative, discard the current window.
### 4. Move start to the next index.
### 5. Update the maximum along the way.
### Important: You don't actually need start to calculate the maximum sum. It's only useful if you also want to return the subarray's boundaries.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        max_sm = nums[0]
        sm = nums[0]

        for end in range(1, len(nums)):
            if sm < 0:
                sm = 0
                start = end

            sm += nums[end]

            if sm > max_sm:
                max_sm = sm

        return max_sm
