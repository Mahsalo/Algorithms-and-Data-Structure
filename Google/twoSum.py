#### Use hashmap or dictionary to track the indices to reduce the runtime from O(n^2) to O(n) and the space would increase from O(1) to O(n) but we care more about the time than space

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in d.keys():
                d[nums[i]] = i
            else:
                return [i,d[diff]]
