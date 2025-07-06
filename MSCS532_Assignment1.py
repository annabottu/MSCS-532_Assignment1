def insertion_sort(array):
    n = len(array)
    #loop through each element in the array starting from the second element
    for i in range(1, n):
        key = array[i]
        j = i - 1
        # Move elements of array[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

array = [5, 2, 9, 1, 5, 6]
insertion_sort(array)
print("Sorted array:", array)
