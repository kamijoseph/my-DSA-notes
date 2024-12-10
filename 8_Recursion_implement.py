
# Simple program to display the recursion of a program

def printFun(test):
    
    if (test < 1):
        return
    else:
        print(test, end=" ")
        printFun(test-1)
        print(test, end=" ")
        return

# Example 2
#Finding factorials

def factorial(n):
    
    # The Base Case of the program
    if n == 1 or n == 0:
        return 1
    
    # The Recursive Case of the Program 
    return n * factorial(n-1)

prompt = input("Enter the number to search for the factorial: ")

if prompt.isdigit():
    prompt = int(prompt)
    result = factorial(prompt)
    print(f"The Factorial of {prompt} is {result}")
else:
    print("Invalid Number")
    

# Example 3
#Fibonacci while using recursion
#    * Formula: F(0)=0,F(1)=1,F(n)=F(n−1)+F(n−2) for n>1

def fib(n):
    # Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + (n-2)
    
prompt2 = input("Enter the number of fibonacci numbers you want added: ")
if prompt2.isdigit():
    prompt2 = int(prompt2)
    fib_results = fib(prompt2)
    print(f"The fibonacci numbers for {prompt2} are {fib_results}")
else:
    print("Invalid Entries!")
    
# For displaying indivindual numbers
def fibonacci(n, current=0, next_val=1):
    
    # Base case: stop when current exceeds n
    if n == 0:
        return
    
    # Print the current Fibonacci number
    print(current, end=" ")
    
    # Recursive case: move to the next Fibonacci number
    fibonacci(n - 1, next_val, current + next_val)

fibonacci(6)  # Output: 0 1 1 2 3 5

# Example 4
 # Reversing a string
def reverse_string(s):
    
    # Base case: if the string is empty or has one character, it's reversed
    if len(s) <= 1:
        return s
    
    # Recursive case: reverse the rest of the string and append the first character
    return reverse_string(s[1:]) + s[0]

# Example Usage
print(reverse_string("hello"))  # Output: "olleh"
