import numpy as np



# 1.Creating lists.

list = ["Boy", "Girl", "dad"]
list2 = [1,3,4,5,6,7]

print(list, list2, "\n\n" )

# Output = ['Boy', 'Girl', 'dad'] [1, 3, 4, 5, 6, 7]
# Access by index , first index being zero.

print(list[0]) # Output: Boy

#Multidimensiona list
list3 = [["Geeks", "For"], ["nerd"]]
print("\n\nMulti-dimenional list: ")
print(list3[1][0])




# 2. Creating Tuples>

# Creating a Tuple with
# the use of Strings
Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)
    
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)

# Accessing element using indexing
print("First element of tuple")
print(Tuple[0])

# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(Tuple[-1])

print("\nThird last element of tuple")
print(Tuple[-3])




# Creating  Sets

Set = set([1, 2, "Kami", 3, 4, "Sama", 6, "Jester"])
print("Set with mixed use of numbers and strings: ")
print(Set)

#Accesing the element using a for loop
for i in (Set):
    print(i, end=" ")
print()

#Checking the element using the in keyword
print("Sama" in Set) 



# Creating a Frozen Sets
# Same as {"a", "b","c"}
normal_set = set(["a", "b","c"])

print("Normal Set")
print(normal_set)

# Creating A frozen set
frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)

# Uncommenting below line would cause error as we are trying to add element to a frozen set
# frozen_set.add("h")



# Creating Dictioaries
# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key
print("Accessing a element using key:")
print(Dict['Name'])

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(1), "\n\n\n")

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict, "\n\n\n")


# Creating a matrix using the numpy library
# Import numpy as np

a = np.array(
    [[1,2,3,4], [4,5,6,7],
     [7,8,9,10], [11,12,13,14]]
)

m = np.reshape(a,(4, 4))
print(m)

# Accessing element
print("\nAccessing Elements: \n")
print(a[1])
print(a[2][0])

# Adding Element
m = np.append(m,[[1, 15,13,11]],0)
print("\nAdding Element: ")
print(m)

# Deleting Element
m = np.delete(m,[1],0)
print("\nDeleting Element")
print(m)



# Creating bytearray
a = bytearray((12, 8, 25, 2))
print("Creating Bytearray:")
print(a)

#Accesing elements
print("\nAccessing the elements:")
print(a[1])

#Appending elements
a.append(30)
print('After appending the bytearray: \n')
print(a, "\n")

#Modifying elements
a[1] = 3
print("\nAfter Modifying:")
print(a)
