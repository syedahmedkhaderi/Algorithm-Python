# Fibonacci formula:
# F(n) = F(n-1) + F(n-2) and F(0) = 0, F(1) = 1

# Naive recursive Fibonacci
def fib_recursive(n):
    # Naive recursive Fibonacci (very slow for large n).
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Memoized Fibonacci (Top-Down DP)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


print("Naive recursive Fibonacci (n=10):", fib_recursive(10))
print("Memoized Fibonacci (n=10):", fib_memo(10))

# Trying larger n to see the difference in performance
print("Memoized Fibonacci (n=50):", fib_memo(50))
