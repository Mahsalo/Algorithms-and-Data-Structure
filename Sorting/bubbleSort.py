#### O(n2) avg and worst (reversely ordered), O(n) best , alreday sorted, O(1) space
#### traverse, compare adjacent elements and swap if needed

def BubbleSort(arr):
    for i in range(len(arr) -1):
        for j in range(len(arr) - i -1):
            if arr[j]>arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr



if __name__=="__main__":
    arr = [2,3,1,5,10,8]
    print(BubbleSort(arr))
