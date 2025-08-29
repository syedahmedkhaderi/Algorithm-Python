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
def insertion_sort3(array):
    count = 0
    for i in range(1, len(array)):
        print(array)
        last_sorted_position = array[i-1]  #We store the last element which is sorted
        count += 1
        if array[i] < last_sorted_position: #We check if the current element is lesser than the last sorted element
            temp = array[i] #If yes, we store the curent element in a temporary variable.
            for j in range(i-1,-1,-1):  #We loop backwards through the sorted part of the array to check where the current element fits
                count += 1
                if temp < array[j]: #For every element we find in the sorted part which is greater than the current element, we shift them one place towards right to make room for the current element
                    if j == 0: #If we reach the beginning of the array in the process, we shift the elements right and we assign the current element to the 0th position
                        array[j+1] = array[j]
                        array[j] = temp
                    else: #Otherwise we just keep shifting
                        array[j+1] = array[j]
                else: #Once we find an element that is smaller than the current element, it means we have found the position to insert out current element at
                    array[j+1] = temp #So we just assign the element to its correct position
                    break #And break out of this loop
    return (f'{array} \nNumber of comparisons = {count}')
