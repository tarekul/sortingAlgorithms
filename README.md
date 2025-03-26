### Bubble Sort vs Merge Sort

Bubble Sort:

- Time Complexity: `O(n^2)`
- Space Complexity: `O(1)`

Merge Sort:

- Time Complexity: `O(n log n)`
- Space Complexity: `O(n)`

Bubble Sort is better for small arrays and is more efficient in terms of space complexity, while Merge Sort is better for larger arrays and is more efficient in terms of time complexity.

### Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

Let's walk through an example:

Bubble Sort:  
[4, 3, 2, 1]

### Pass 1 (Largest element moves to the right)

| Comparisons | Array        | Swap?   |
| ----------- | ------------ | ------- |
| 4 vs 3      | [3, 4, 2, 1] | ✅ Swap |
| 4 vs 2      | [3, 2, 4, 1] | ✅ Swap |
| 4 vs 1      | [3, 2, 1, 4] | ✅ Swap |

🔹 Total comparisons in Pass 1: 3

[3, 2, 1, 4]

### Pass 2 (Second largest element moves to the right)

| Comparisons | Array        | Swap?   |
| ----------- | ------------ | ------- |
| 3 vs 2      | [3, 2, 4, 1] | ✅ Swap |
| 3 vs 1      | [3, 2, 1, 4] | ✅ Swap |

🔹 Total comparisons in Pass 2: 2

[2 , 1, 3, 4]

### Pass 3 (Third largest element moves to the right)

| Comparisons | Array        | Swap?   |
| ----------- | ------------ | ------- |
| 2 vs 1      | [2, 1, 3, 4] | ✅ Swap |

🔹 Total comparisons in Pass 3: 1

Final Sorted Array: [1, 2, 3, 4]
Total Comparisons: 3 + 2 + 1 = 6

### Merge Sort

Merge Sort is a divide-and-conquer algorithm that splits the array into two halves, recursively sorts each half, and then merges the sorted halves back together. It is a stable sorting algorithm with a time complexity of `O(n log n)` and a space complexity of `O(n)`.

Let's walk through an example:

Merge Sort:  
[4, 3, 2, 1]

### Pass 1 (Splitting the array into two halves)

| Left Half | Right Half |
| --------- | ---------- |
| [4, 3]    | [2, 1]     |

🔹 Splits in pass 1: 1

### Pass 2 (Splitting further)

| Left Half | Right Half | Left Half | Right Half |
| --------- | ---------- | --------- | ---------- |
| [4]       | [3]        | [2]       | [1]        |

🔹 Splits in pass 2: 2

### Pass 3 (Sorting individual elements)

| Left Half | Right Half | Merged Result |
| --------- | ---------- | ------------- |
| [4] [3]   |            | [3, 4]        |
|           | [2] [1]    | [1, 2]        |

🔹 Comparisons in pass 3: 2

### Pass 4 (Merging the sorted halves)

| Left Half | Right Half | Merged Result |
| --------- | ---------- | ------------- |
| [3, 4]    | [1, 2]     | [1, 2, 3, 4]  |

🔹 Comparisons in pass 4: 2

Final Sorted Array: [1, 2, 3, 4]
Total Comparisons: 2 + 2 = 4
Total Merges: 2 + 1 = 3
Total Swaps: 1 (Pass 3) + 1 (Pass 3) = 2 swaps

Bubble Sort:

- Time Complexity: `O(n^2)`
- Space Complexity: `O(1)`
- Total Comparisons: 6

Merge Sort:

- Time Complexity: `O(n log n)`
- Space Complexity: `O(n)`
- Total Comparisons: 4
