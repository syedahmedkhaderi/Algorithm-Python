# Memoization is storing results of function calls so that if the same input occurs again,
# we return the stored result instead of recomputing.


# Example 1: Factorial with Memoization
def factorial(n, memo={}):
    if n in memo:
        return memo[n]  # return cached result

    if n <= 1:
        return 1

    # store result in memo before returning
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]

print("Factorial of 5:", factorial(5))
print("Factorial of 6 (uses memo):", factorial(6))


# Example 2: Counting Paths in a Grid (classic DP problem)
def grid_paths(m, n, memo={}):
    # Count unique paths in an m x n grid.
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 1 or n == 1:
        return 1

    memo[(m, n)] = grid_paths(m - 1, n, memo) + grid_paths(m, n - 1, memo)
    return memo[(m, n)]

print("Unique paths in a 3x3 grid:", grid_paths(3, 3))
