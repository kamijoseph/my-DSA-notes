
# Define the maximum size for the dp array
MAXN = 100  # You can adjust this as needed

# Function to compute factorials using dynamic programming
def compute_factorials(n):
    # Initialize the dp array
    dp = [0] * MAXN
    # Base case: 0! = 1
    dp[0] = 1
    
    # Fill the dp array using the recursive relation
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    
    return dp[:n + 1]

# Input: Compute factorials up to n
n = int(input("Enter a number to compute factorials up to: "))

# Call the function
factorials = compute_factorials(n)

# Display the results
print(f"Factorials from 0! to {n}!:")
for i in range(n + 1):
    print(f"{i}! = {factorials[i]}")
    
# Example 2
# down top approach Fibonacci using dynamic programming

def fibb(n):
    if n == 1 or n == 0:
        return n
    
    # Initialize a table to store the Fibonacci numbers
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    
    # Build the table from the bottom up
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    
    return fib_table[n]

print(fibb(6))

# Example 2: Fibonacci Sequence (Top-Down Approach)
def fibonacci_memo(n, memo=None):
    # Initialize memo dictionary if it's the first call
    if memo is None:
        memo = {}
    
    # Base case: return n if it's 0 or 1
    if n == 0 or n == 1:
        return n
    
    # If the result is already in memo, return it
    if n in memo:
        return memo[n]
    
    # Otherwise, compute the Fibonacci number and store it in memo
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Example Usage
print(fibonacci_memo(6))  # Output: 8

# Example 3: Longest common Subsequent
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D table to store the lengths of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table using the bottom-up approach
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # Characters match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Take the max from the left or top
    
    # The value in dp[m][n] is the length of the LCS
    return dp[m][n]

# Example Usage
X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y))  # Output: 4
