#### Minimum length of a sub-array of positive integers that has a sum >= a given positive target


def MinLengthSum(nums, target):
    if not nums:
        return 0
    for i in range(len(nums)):  # O(n) time
        if nums[i] >= target:
            return 1
    if sum(nums) < target:
        return 0

    s = 0
    e = 0
    sm = 0
    minL = len(nums)

    while e < len(nums):
        if sm < target:
            sm = sm + nums[e]
            e += 1
        else:  # condition met - keep shrinking while valid
            while sm >= target:
                L = e - s
                if L < minL:
                    minL = L
                sm = sm - nums[s]
                s += 1

    # FIXED: Added the shrinking loop here so the final window gets squeezed too
    while sm >= target:
        L = e - s
        if L < minL:
            minL = L
        sm = sm - nums[s]
        s += 1
    return minL

if __name__ == "__main__":
    nums = [2,1,5,1,5,3]
    target = 10  #fixed size of the subarray
    print(MinLengthSum(nums, target))
    print(MinLengthSum([1,2,1], 5))
    print(MinLengthSum([2,3,1,2,4,3], 7))

