### Easy: since you can have extra space to store data
def RemoveDuplicateSorted(nums):
    p1 = 0
    p2 = 1
    d = [nums[p1]]

    while p2<len(nums):
        if nums[p1] == nums[p2]:
            p2 = p2+1
        else:
            d.append(nums[p2])
            p1 = p2
            p2 = p2+ 1
    diff = len(nums) - len(d)
    for i in range(diff):
        d.append("_")

    return d


N = [1,1,1,2,2,2,2,2,5,5,5,7,7,7,8]
print(RemoveDuplicateSorted(N))
