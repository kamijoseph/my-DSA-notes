
# heap sort algorithm implementation

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def siftDown(array, i, upper):
    while True:
        left = i * 2 + 1
        right = i * 2 + 2
        if max(left, right) < upper:
            if array[i] >= max(array[left], array[right]):
                break
            elif array[left] > array[right]:
                swap(array, i, left)
                i = left
            else:
                swap(array, i, right)
                i = right
        elif left < upper:
            if array[left] > array[i]:
                swap(array, i, left)
                i = left
            break
        elif right < upper:
            if array[right] > array[i]:
                swap(array, i, right)
                i = right
            break
        break

def heapSort(array):
    pass