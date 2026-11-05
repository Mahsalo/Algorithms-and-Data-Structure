#### At each pass(i), select the minimum in the remaining part of the array, compare with the current and swap if needed
#### O(n2) avg, best, worst
#### selection sort
def SelectionSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr



if __name__=="__main__":
    arr = [2,3,1,5,10,8]
    arr_2 = [9,4,10,0,1,4,2]
    print(SelectionSort(arr_2))
