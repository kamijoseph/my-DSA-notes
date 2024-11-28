
def merge_sort(array):
    
    #Base case: A single element is already sort
    if len(array) <= 1:
        return array
    
    #Divide the array into two halves
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
        # Add any remaining elements from the left or right subarray
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", numbers)
sorted_numbers = merge_sort(numbers)
print("Sorted List:", sorted_numbers)