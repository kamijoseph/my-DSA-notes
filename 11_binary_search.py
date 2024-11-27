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
