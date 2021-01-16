def quickSort(arr):
    #递归
    length = len(arr)
    if(length<2):
        return arr
    else:
        mid = arr[length//2]
        left,right = [],[]
        arr.remove(mid)
        for i in arr:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        return quickSort(left)+mid+quickSort(right)


arr = [3, 2, 0, 7, 4]
result = quickSort(arr)
print(result)