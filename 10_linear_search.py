
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