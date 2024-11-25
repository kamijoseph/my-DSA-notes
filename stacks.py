
stack = []

# append() function to push an element in the stack
stack.append("F")
stack.append("G")
stack.append("F")

print("Initial Stack: ")
print(stack)

# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)