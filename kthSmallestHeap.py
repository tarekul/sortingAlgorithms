def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
        
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
    

def kthSmallestHeap(arr, k):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(1, k):
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        n -= 1
        heapify(arr, n, 0)
    
    return arr[0]
    

print(kthSmallestHeap([5, 4, 3, 2, 1], 3)) # 3
print(kthSmallestHeap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 50, 25, 75, 150, 200, 300, 400, 250, 350], 18)) # 300
