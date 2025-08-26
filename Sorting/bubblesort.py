def bubble_sort(array):
    count = 0
    for i in range(len(array)-1): #-1 because when only 1 item will be left, we don't need to sort that
        print(array)
        for j in range(len(array)-i-1): #In every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
            count += 1
            if array[j] > array[j+1]: #If two adjacent elements in the wrong order are found, they are swapped
                array[j], array[j+1] = array[j+1], array[j]
    #print(f'Number of comparisons = {count}')
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(bubble_sort(array))

'''
[5, 9, 3, 10, 45, 2, 0]
[5, 3, 9, 10, 2, 0, 45]
[3, 5, 9, 2, 0, 10, 45]
[3, 5, 2, 0, 9, 10, 45]
[3, 2, 0, 5, 9, 10, 45]
[2, 0, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45]
Number of comparisons = 21
'''