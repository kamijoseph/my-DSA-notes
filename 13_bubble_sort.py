
def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        swapped = False
        # Perform a single pass of the bubble sort
        for j in range(n - i - 1):  # Last i elements are already sorted
            if array[j] > array[j + 1]:
                # Swap if elements are in the wrong order
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                
        # If no two elements were swapped, the list is sorted
        if not swapped:
            break
    return array


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted List:", sorted_numbers)