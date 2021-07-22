# """ un/comment to de/activate ###########################

# overview
# data types
    # int, float
    # bool
    # str
    # None
    # tuple *

    # list
    # set  *
    # dict *

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else
    # <, >, ==, !=, >=, <=,
    # not, and, or

# iteration
    # for
    # while


####################################################### """
""" un/comment to de/activate ###########################

# for loops
# the gauntlet of primes
# boolean flags
# is_prime
'''
tell me if a number is prime or not

parameters / arguments / inputs
n <int>

return / output
<bool> True if n is prime else false
'''
# def is_prime(n):
#     if n < 2:
#         return False
#
#     prime = True # flag
#     for i in range(2, int(n / 2) + 1):
#         if n % i == 0:
#             prime = False
#             break
#
#     return prime

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False

    return True

# print("start")
# i = 100_000_000
# print( i, is_prime(i) )
# print("stop")

# for i in range(0, 20):
#     print( i, is_prime(i) )

# next_prime
'''
inputs
n <int>:

outputs
<int>: the next prime number after n

notes
takes n and returns the next prime number after n
if n is prime it DOES NOT return n
'''

# def next_prime(n):
#     if n < 2:
#         return 2
#     while True:
#         n += 1
#         prime = True
#         for i in range(2, int(n / 2) + 1):
#             if n % i == 0:
#                 prime = False
#         if prime:
#             return n


def next_prime(n):
    while not is_prime(n + 1):
        n += 1

    return n + 1

for i in range(0, 20):
    print( i, next_prime(i) )


# nth_twin_prime_pair

####################################################### """
""" un/comment to de/activate ###########################

for i in range(10):
    if i == 0:
        continue # skip
    print( 100 / i )

####################################################### """
