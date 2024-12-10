
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted array
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

numbers = [64, 25, 12, 22, 11]
print("Unsorted List:", numbers)
sorted_numbers = selection_sort(numbers)
print("Sorted List:", sorted_numbers)

