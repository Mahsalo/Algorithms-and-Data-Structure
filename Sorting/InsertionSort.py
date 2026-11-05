#### Standard Insertion sort: each pass has a key (element at the ith position): compare the key with all left elements
#### while its smaller, shift the left keys to the righ, when becomes bigger, insert that key
#### O(n2) time

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

    return arr



if __name__=="__main__":
    arr = [2,3,1,5,10,8]
    arr_2 = [9,4,10,0,1,4,2]
    print(InsertionSort(arr_2))
