
# Simple code to show a linear search in a sorted array
def search(array, size, target):
    for i in range(0, size):
        if (array[i] == target):
            return i
    return -1

array = [3,4,6,10,30,40]
target = int(input("Enter target value: "))
size = len(array)

result = search(array, size, target)
if result == -1:
    print("Target value does not exist in the array.")
else:
    print(f"Target value is at index, {result}")
    
#The time complexity of the above algorithm is O(n).

# Code 2
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

arr = [3,4,6,10,30,40]
target = 6

results = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {results}.")
else:
    print(f"Element {target} was not found.")