def binarySearch(array, left, right, target):
    # Base case: If the range is invalid
    if left > right:
        return -1

    # Find the middle index
    mid = left + (right - left) // 2

    # Check if target is at mid
    if array[mid] == target:
        return mid

    # If target is smaller than mid, search in the left subarray
    elif array[mid] > target:
        return binarySearch(array, left, mid - 1, target)

    # Otherwise, search in the right subarray
    else:
        return binarySearch(array, mid + 1, right, target)

# Example usage
array = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter the target value: "))

# Call binary_search
result = binarySearch(array, 0, len(array) - 1, target)

# Print the result
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

# Code 2
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return mid
        
        # if target is bigger than mid, ignore the left side of the array
        elif arr[mid] < target:
            low = mid + 1
        
        # If target is smaller, ignore the right half
        else:
            high = mid - 1
    return -1 # Target Not Found

arr = [2, 5, 6, 7, 8, 10, 12]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array.")