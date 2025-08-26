# Recursive Approach
def fibo1(n):
    if (n < 2):
        return n
    return fibo1(n-1) + fibo1(n-2)

# Iterative Approach
def fibo2(n):
    arr = [0,1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr
    
'''
O(2^n) for recursive approach which is horrible and very terrible.
O(n) for iterative approach.
'''