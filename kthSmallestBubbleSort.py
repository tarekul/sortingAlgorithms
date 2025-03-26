def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def kthSmallestBubbleSort(arr, k):
    bubbleSort(arr)
    return arr[k-1]
    
"""
n = 20 (number of elements in list)
Pass 1: 19 comparisons
Pass 2: 18 comparisons
Pass 3: 17 comparisons
Pass 4: 16 comparisons
Pass 5: 15 comparisons
Pass 6: 14 comparisons
Pass 7: 13 comparisons
Pass 8: 12 comparisons
Pass 9: 11 comparisons
Pass 10: 10 comparisons
Pass 11: 9 comparisons
Pass 12: 8 comparisons
Pass 13: 7 comparisons
Pass 14: 6 comparisons
Pass 15: 5 comparisons
Pass 16: 4 comparisons
Pass 17: 3 comparisons
Pass 18: 2 comparisons
Pass 19: 1 comparison
Total: 190 comparisons


To sort the array we need to do 190 comparisons = 190 operations.
To get the kth smallest number we just access the k-1 index of the sorted array. 
"""
print(kthSmallestBubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 50, 25, 75, 150, 200, 300, 400, 250, 350]
, 18)) # 300

