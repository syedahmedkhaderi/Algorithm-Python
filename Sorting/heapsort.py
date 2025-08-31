count = 0
def max_heapify(arr, heap_size, node):
    left = 2 * curr + 1
    right = 2 * curr + 2
    curr = node

    if arr[curr] < arr[left] and curr < heap_size:
        count += 1
        curr = left
    
    if arr[curr] < arr[right] and curr < heap_size:
        count += 1
        curr = right
    
    if curr != node:
        arr[node], arr[i] = arr[i], arr[node]
        max_heapify(arr, heap_size, node)
    
def build_heap(arr):
    heap_size = len(arr)
    for i in range(heap_size//2, -1, -1):
        max_heapify(arr, heap_size, i)

