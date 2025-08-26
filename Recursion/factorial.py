# Non Recursive Approach

def fact1(number):
    i = 1
    for j in range(1, number + 1):
        i *= j
    print(i)

fact1(5)
# 120

# Recursion
def fact2(number):
    if number == 2:
        return 2
    return number * fact2(number - 1)

print(fact2(6))

# Both are O(n)
