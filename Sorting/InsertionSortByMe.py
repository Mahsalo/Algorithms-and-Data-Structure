#### insertion sort: but it has unnecessary swapping
#### O(n2)
def InsertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i]<arr[j]: # j shows the left part
                arr[i], arr[j] = arr[j], arr[i]
    return arr



if __name__=="__main__":
    arr = [2,3,1,5,10,8]
    arr_2 = [9,4,10,0,1,4,2]
    print(InsertionSort(arr_2))
