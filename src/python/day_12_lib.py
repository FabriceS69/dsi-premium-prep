""" un/comment to de/activate ###########################
# workflow
# eg of global vs local
# while -> for

'''
Write a function that computes and returns a list of all of the divisors of some positive integer.
    * Use a while loop.
    * Things to think about:
        * How do you determine if a single number is a divisor of another?
* What is your stopping condition?
* BONUS: rewrite this with a for loop
'''
# ION, input, output, notes

def divisors_list(n):
    lst = []
    i = 0
    while i < n:
        i += 1
        if n % i == 0:
            lst.append(i)

    return lst


for i in range(10):
    res = divisors_list(i)
    print( i, len(res), res )

####################################################### """
""" un/comment to de/activate ###########################

# overview
# data types
# abstractions
# control flow
    # if
# iteration
    # while

# if condition:
#     conclusion

# while condition:
#     conclusion

####################################################### """
""" un/comment to de/activate ###########################

def is_prime(n):
    if n < 2: return False

    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0: return False

    return True


def next_prime(n):
    while not is_prime(n + 1):
        n += 1

    return n + 1

i = 342
print( i, next_prime(i) )

# for i in range(20):
    # print(i, next_prime(i) )

####################################################### """
""" un/comment to de/activate ###########################
### data structures
# dictionaries
# sets
# tuples

# overview
# data types
    # int, float
    # bool
    # str
    # None
    #! tuple

    # list
    #! dict
    #! set

# abstractions
# control flow
    # if
# iteration
    # while

####################################################### """
""" un/comment to de/activate ###########################

print(dir([]))
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(dir(()))
['count', 'index']

####################################################### """
""" un/comment to de/activate ###########################

# CRUD

# print("\nlist")
lst = [44, 55, 77, 55]
# print( lst )
# print( lst[1] ) # 55

# for idx, ele in enumerate(lst):
#     print(idx, ele)

# print(lst)
# lst.append("hello")
# print(lst)

print("\ndictionary")
d = {
    "a": 44 ,
    "b": 55 ,
    "c": 77 ,
    "d": 55 ,
}

# print( d )
# print( d["b"] ) # 55

# for key, val in d.items():
#     print(key, val)

# print( d )
# d["e"] = "hello"
# print( d )

# print( d )
# # del d["c"]
# res = d.pop("c")
# print( res )
# print( d )

####################################################### """
""" un/comment to de/activate ###########################

class myClass:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"{self.n}"

print( myClass(42) )

####################################################### """
""" un/comment to de/activate ###########################

# class itself is not a type, but it makes types
class uint:
    def __init__(self, n):
        self.n = abs(n)

    def __repr__(self):
        return f"{self.n}"


# uint is the type I made with the class above
print( uint(-42) )


####################################################### """
""" un/comment to de/activate ###########################

def is_prime(n):
    if n < 2: return False

    for i in range( 2, int(n**(1/2)) + 1 ):
        if n % i == 0: return False

    return True


print( is_prime(9) ) # False

####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
