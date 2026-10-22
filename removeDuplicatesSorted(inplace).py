def removeDuplicatesSortedInplace(N):
    if not N:
        return N
    i, j = 0, 1
    k = 1
    print(len(N))
    while j < len(N):
        if N[i] != N[j]:
            i = i + 1
            N[i] = N[j]
            k = k + 1
        j = j + 1

    d = len(N) - k
    if d>0:
        N[-d:] = ["_"]*d
    return N

if __name__ == "__main__":
    N = [0,0,1,1,1,1,2,3,4,5,6,6,6,6,7]
    print(removeDuplicatesSortedInplace(N))
    print(removeDuplicatesSortedInplace([]))
