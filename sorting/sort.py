# 冒泡排序
# 冒泡：每一次循环将最大值放（冒）到最右边，从右向左的数是已经排好的
# 外层循环n次
# 内层从第1个数开始比较，后第n个数已经是排好序的。
# 平均时间复杂度：O(n^2)， 最好时间复杂度：O(n) 最坏时间复杂度：O(n^2) 空间复杂度：O(1)
def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 每一次循环， 都把最小值放在最左边
# 左边第i个数已经排序好
# 平均时间复杂度：O(n^2)， 最好时间复杂度：O(n^2) 最坏时间复杂度：O(n^2) 空间复杂度：O(1)
def selectionSort(arr):
    n = len(arr)

    for i in range(0, n):
        min_index = i
        for j in range(i, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

# 将第一待排序序列第一个元素看做一个有序序列,把第二个元素到最后一个元素当成是未排序序列。

# 从头到尾依次扫描未排序序列将扫描到的每个元素插入有序序列的适当位置。（
# 如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
# 平均时间复杂度：O(n^2)， 最好时间复杂度：O(n) 最坏时间复杂度：O(n^2) 空间复杂度：O(1)
def intersectionSort(arr):
    n = len(arr)
    for j in range(1, len(arr)):  # 从list第二个元素开始
        key = arr[j]  # 储存将要进行插入排序的元素数值
        index = j  # 储存将要进行插入排序的元素的索引
        while index > 0 and arr[index - 1] > key:  # 执行插入排序的判断条件
            arr[index] = arr[index - 1]  # 将之前排好序的元素向后移
            index -= 1
        arr[index] = key  # 以上将元素向后移后，将新加元素插入它的正确的位置上

