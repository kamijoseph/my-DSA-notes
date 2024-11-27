
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
    

