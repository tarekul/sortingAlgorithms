def kthSmallestNaive(arr, k):
    for i in range(k):
        min = arr[0]
        for j in range(1, len(arr)):
            if arr[j] < min:
                min = arr[j]
        arr.remove(min)
    return min
    
    
"""
We are doing k = 18 loops and in each loop we are removing the minimum element.
Loop 1: 19 comparisons
Loop 2: 18 comparisons
Loop 3: 17 comparisons
Loop 4: 16 comparisons
Loop 5: 15 comparisons
Loop 6: 14 comparisons
Loop 7: 13 comparisons
Loop 8: 12 comparisons
Loop 9: 11 comparisons
Loop 10: 10 comparisons
Loop 11: 9 comparisons
Loop 12: 8 comparisons
Loop 13: 7 comparisons
Loop 14: 6 comparisons
Loop 15: 5 comparisons
Loop 16: 4 comparisons
Loop 17: 3 comparisons
Loop 18: 2 comparisons
Loop 19: 1 comparison
Total: 190 comparisons

To get the kth smallest we have to do 190 comparisons = 190 operations. 
"""

print(kthSmallestNaive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 50, 25, 75, 150, 200, 300, 400, 250, 350], 18)) # 300