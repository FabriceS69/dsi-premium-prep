""" un/comment to de/activate ###########################

# raise each value in lst to the power of it index
lst = [4, 3, 99, 2, 7, 99, 6]
#      0, 1, 2,  3, 4, 5,  6

for pair in enumerate(lst):
    print(pair)

# for num in lst:

####################################################### """
""" un/comment to de/activate ###########################

# overview
# data types
    # int, float
    # bool
    # str
    # None
    # tuple

    # list

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else

# iteration
    # for
    # while <-------


# syntax
# problem solving
# workflow


# project
# factorial
# input  <int>
# return <int>
# notes: computes and returns the factorial of n

# def factorial(n):
#     prod = 1
#
#     return prod


# print(factorial(4)) # 24

####################################################### """
""" un/comment to de/activate ###########################

# a = 10
# b = 5
# if a > b:
#     print("a is greater than b")


controller = 0
while True: # run forever
    controller += 1
    print(controller)
    if controller >= 4:
        break

####################################################### """
""" un/comment to de/activate ###########################

'''
squares_lst

input: <list<num>>

output: <list<num>>

notes: calculates the square of each number in the input lst and appends it to the output
'''

def squares_lst(lst):
    squares = []
    for num in lst:
        squares.append(num**2)

    return squares


print( squares_lst([2, 3, 4]) ) # [4, 9, 16]
# print( squares_lst([4, 5, 3, 6, 2, 7, 6]) ) # []

####################################################### """
""" un/comment to de/activate ###########################

'''
is_prime

input n <int>

return <bool>

notes:
    determines if n is prime or not and returns a bool accordingly
    if n is prime -> True
    if n is not prime -> False
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range( 2, int(n**(1/2)) + 1 ):
        if n % i == 0:
            return False

    return True


# for i in range(20):
#     print( i, is_prime(i) )


'''
next_prime

input n <int>

return <int>

notes:
    locates the next prime number after n and returns that number
    n = 12 -> 13
    n = 13 -> 17
    n = 14 -> 17
'''

def next_prime(n):
    while not is_prime(n+1):
        n += 1

    return n + 1


prime_windows_lst = []
for i in range(2000):
    if is_prime(i):
        prime_windows_lst.append( next_prime(i) - i )

print( sum(prime_windows_lst) / len(prime_windows_lst) )

####################################################### """
# """ un/comment to de/activate ###########################

def get_divisors(n):
    lst = []
    i = 0
    while i+1 <= n:
        i += 1
        if n % i == 0:
            lst.append(i)

    return lst

for i in range(20):
    print( i, get_divisors(i) )


def get_divisors(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)

    return lst


for i in range(20):
    print( i, get_divisors(i) )

####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
