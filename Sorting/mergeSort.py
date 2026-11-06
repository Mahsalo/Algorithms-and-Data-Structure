#### Merge Sort
#### 1) divide (O(logn)) find mid point and left and right array then recursively call itself (division)
#### 2) zipper/merge (O(n)) compare left side of each right and left and if smaller append the results, take care of the remaining portion
#### total: O(nlogn) time and O(n) space


def division(a):
    ## this part really important since you stop at the leaves
    if len(a)<=1:
        return a
    mid = len(a)//2
    left_a = a[:mid]
    right_a = a[mid:]

    sorted_left = division(left_a)
    sorted_right = division(right_a)

    # reached the leaves
    return zipper(sorted_left, sorted_right)

def zipper(l, r):
    res = []
    i, j = 0, 0

    while i<len(l) and j<len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i+=1
        elif l[i] > r[j]:
            res.append(r[j])
            j+=1
    res.extend(l[i:])
    res.extend(r[j:])
    return res


if __name__ == "__main__":
    a = [43,0,2,1,11,34]
    print(division(a))
