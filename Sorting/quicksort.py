#Quick Sort is another sorting algorithm which follows divide and conquer approach.
#It requires to chose a pivot, then place all elements smaller than the pivot on the left of the pivot and all elements larger on the right
#Then the array is partitioned in the pivot position and the left and right arrays followthe same procedure until the base case is reached.
#After each pass the pivot element occupies its correct position in the array.
#Time Complexity in Best and Average cases is O(nlog N) whereas in worst case it jumps up to O(n^2). Space complexity is O(log n)

#In this implementation, we will take the last element as pivot.

def quicksort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    items_greater = []
    items_lower = []

    for element in arr:
        if element > pivot:
            items_greater.append(element)
        else:
            items_lower.append(element)
        
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))

