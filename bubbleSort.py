def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubbleSort([64, 34, 25, 12, 22, 11, 90])) # [11, 12, 22, 25, 34, 64, 90]
        
"""
Time Complexity: O(n^2)
Space Complexity: O(1)

[64, 34, 25, 12, 22, 11, 90], n = 7 -> O(7^2) = 49 comparisons
"""