
def quick_sort(array):
    
    #Base case . If array is empty or less than one it is sorted.
    if len(array) <= 1:
        return array
    
    # Choose the pivot (Last element here)
    pivot = array[-1]
    
    # Partition into two subarrays
    left = [x for x in array[:-1] if x <= pivot]  # Elements <= pivot
    right = [x for x in array[:-1] if x > pivot]  # Elements > pivot
    
    # Recursively apply QuickSort to the subarrays and combine
    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", numbers)
sorted_numbers = quick_sort(numbers)
print("Sorted List:", sorted_numbers)