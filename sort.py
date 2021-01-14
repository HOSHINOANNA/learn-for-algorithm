# 冒泡排序
# 冒泡：每一次循环将最大值放（冒）到最右边，从右向左的数是已经排好的
# 外层循环n次
# 内层从第1个数开始比较，后第n个数已经是排好序的。
# 平均时间复杂度：O(n^2)， 最好时间复杂度：O(n) 最坏时间复杂度：O(n^2) 空间复杂度：O(1)
def bubbleSort(arr):
    n = len(arr)
    for i in range(0,n):
        print(i)
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [3, 2, 0, 7, 4]
bubbleSort(arr)
