#In Insertion sort, for the first iteration we fix the first element, assuming it is at its correct position
#Then we loop through the rest of the elements and insert them in their correct positions, with respect to the alreay sorted part of the array
#Time complexity is O(n^2) in worst case
def insertion_sort(arr):
    end = arr[0]
    i = 1
    count = 0
    while i < len(arr):
        count += 1
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j,x)
                    break
        end = arr[i]
        i += 1
    return f" {arr}, No. of passes: {count}"

array = [5,9,3,10,45,2,0]
print(insertion_sort(array))

sorted_array = [5,6,7,8,9]
print(insertion_sort(sorted_array))
#It is fast for sorted or nearly sorted inputs as can be seen with the number of comparisons above.

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
print(insertion_sort(reverse_sorted_array))







# Method 2
def insertion_sort2(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to insert
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        arr[j + 1] = key   # Place key at correct position
    return arr

# Example usage:
arr = [11, 9, 3, 10, 45, 2, 0]
print("Sorted array:", insertion_sort2(arr))







# Method 3
def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1

    return list_a



print(insertion_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8]))