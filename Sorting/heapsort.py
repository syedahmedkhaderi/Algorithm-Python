#Heap Sort as the name suggests, uses the heap data structure.
#First the array is converted into a binary heap. Then the first element which is the maximum elemet in case of a max-heap,
#is swapped with the last element so that the maximum element goes to the end of the array as it should be in a sorted array.
#Then the heap size is reduced by 1 and max-heapify function is called on the root.
#Time complexity is O(nlog N) in all cases and space complexity = O(1)

count = 0
def max_heapify(arr, heap_size, node):
    # Find largest among root, left child and right child
    curr = node
    left = 2 * curr + 1
    right = 2 * curr + 2

    global count

    if left < heap_size and arr[curr] < arr[left]:
        count += 1
        curr = left
    
    if right < heap_size and arr[curr] < arr[right]:
        count += 1
        curr = right
    
    # Swap and continue heapifying if root is not largest
    if curr != node:
        arr[node], arr[curr] = arr[curr], arr[node]
        max_heapify(arr, heap_size, curr)

def heap_sort(arr):
    heap_size = len(arr)
    #Converting array to heap.
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(arr, heap_size, i)
    print(f"Heap: {arr}")
    # Now comes heap sort:
    for i in range(heap_size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        max_heapify(arr, i, 0)
    
    return arr

arr = [5, 9, 3, 10, 45, 2, 0]
print(heap_sort(arr))
# Output: [0, 2, 3, 5, 9, 10, 45]