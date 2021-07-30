
def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod

# print(1 / factorial(10))


def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

def permutations(n, k):
    perm = 1
    for i in range(n-k, n+1):
    # for i in range((n-k)+1, n+1):
        perm *= i
    return perm

# print(permutations(10, 4))


