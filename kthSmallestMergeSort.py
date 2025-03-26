def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr

def kthSmallestMergeSort(arr, k):
    mergeSort(arr)
    return arr[k-1]

"""
Split
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 50, 25, 75, 150, 200, 300, 400, 250, 350]

We have log (n=20) = 4.32 ~ 5 splits
Time complexity is O(n log n) = 20 * 5 = 100 operations

To get the kth smallest number we just access the k-1 index of the sorted array.
"""
    
print(kthSmallestMergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 50, 25, 75, 150, 200, 300, 400, 250, 350]
, 18)) # 300