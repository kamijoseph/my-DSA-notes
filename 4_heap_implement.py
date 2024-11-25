
import heapq

#Initialize list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

#Printing created heap
print("The created heap is:", end=" ")
print(list(li))

#Using heappush() to push elements into the heap, 4 pushes.
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))