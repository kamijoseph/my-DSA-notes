
def shell_sort(array):
    n = len(array)
    gap = n // 2  # Initialize the gap
    
    # Reduce the gap and sort the subarrays
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            # Perform a gapped insertion sort
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
            
        # Reduce the gap for the next iteration
        gap //= 2

    return array

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", numbers)
sorted_numbers = shell_sort(numbers)
print("Sorted List:", sorted_numbers)