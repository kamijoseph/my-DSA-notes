
def insertion_sort(array):
    for i in range(1, len(array)):
        
        #Store the current element
        key = array[i]
        j = i-1
        
        # Move elements of the sorted part that are greater than the key
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        # Place the key in its correct position
        array[j + 1] = key
    return array

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", numbers)
sorted_numbers = insertion_sort(numbers)
print("Sorted List:", sorted_numbers)