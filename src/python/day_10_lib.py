# """ un/comment to de/activate ###########################

# reminder to apply

# importing
# https://learn-2.galvanize.com/cohorts/2508/blocks/315/content_files/06_Importing/00_unit_overview.md

# import math
# print( dir(math) )
# help( math )

# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# print( math.cos(0.22) )
# import random

# overview
# data types
    # int, float
    # bool
    # None
    # str

    # list

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else
    # conditions
    # conclusions

# iteration
    # for
    # while

####################################################### """
# """ un/comment to de/activate ###########################

## help()
## dir()

# lst = [4, 3, 6, 2, 7]

## len()
# lst = [4, 3, 6, 2, 7]
# print( len(lst) )

## sum()
# lst = [4, 3, 6, 2, 7]
# print( sum(lst) )
# print( sum(["hello", "world"]) ) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print( sum([4, 3, 6, 5, 99, 2 "7"]) ) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

## max()
## min()
# lst = [4, 3, 6, 2, 7]
# print( max(lst) )
# print( min(lst) )
# print( max( ["dog", "apple", "banana", "cat"] ) )
# print( min( ["apple", "banana", "cat", "dog"] ) )

## all()
## any()
# print( all([0, 5, 7]) )
# print( all([1, 5, 7]) )
# print( any([0, 5, 7]) )
# print( any([1, 5, 7]) )
# print( any([0, 0.0, ""]) )

## .sort()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
# print( lst.sort() )
# print( id(lst), lst )

## .reverse()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
# print( lst.reverse() )
# print( id(lst), lst )

## sorted()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
# lst = sorted(lst)
# print( id(lst), lst )
# print( id(lst), lst )

## reversed()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
# rev_lst = list(reversed(lst))
# print( id(rev_lst), rev_lst )
# print( id(lst), lst )

# for i in reversed(lst):
#     print(i)

# lst = [4, 3, 6, 2, 7]
# print( lst[::-1] )

## .append()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
# print( lst.append(57) )
# print( id(lst), lst )

## .extend()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
## print( lst.append([57, 63, 99]) ) # [4, 3, 6, 2, 7, [57, 63, 99]]
# print( lst.extend([57, 63, 99]) ) # [4, 3, 6, 2, 7, 57, 63, 99]
# print( id(lst), lst )

## .insert()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
# print( lst.insert(3, "hello") )
# print( id(lst), lst )

## .remove()
# lst = [4, 3, 99, 2, 7, 99, 6]
# print( id(lst), lst )
# element_to_remove = 99
# print( lst.remove(99) )
# print( id(lst), lst )

## .pop()
# lst = [4, 3, 6, 2, 7]
# print( id(lst), lst )
# index_to_pop = 2
# print( lst.pop(index_to_pop) )
# print( id(lst), lst )

## .count()
# lst = [4, 3, 99, 2, 7, 99, 6]
# print( lst.count(99) )
# print( lst.count(7) )
# print( lst.count(1000) )
# print( lst.count("hello") )

# use .count() and .remove() together
# lst = [4, 3, 99, 2, 7, 99, 6]
# remove = 99
# for _ in range(lst.count(remove)): #
#     print( lst.remove(remove) )

## .index()
# lst = [4, 3, 99, 2, 7, 99, 6]
# print( id(lst), lst )
# print( lst.index(4) )
# print( lst.index(3) )
# print( lst.index(99) )
# print( lst.index(2) )

## enumerate()
lst = [4, 3, 99, 2, 7, 99, 6]
# print("iterate through elements")
# for ele in lst:
#     print(ele)
#
# print("iterate through indicies")
# for idx in range( len(lst) ):
#     print(idx)
#
# print("iterate through indicies AND elements")
# for idx, ele in enumerate(lst):
#     print(idx, ele)
#
#
# print("iterate through indicies AND elements")
# for idx, ele in enumerate(lst, 2):
#     print(idx, ele)


# lst = [4, 3, 99, 2, 7, 99, 6]
# print( list(enumerate(lst)) )
# enum_lst = [(0, 4), (1, 3), (2, 99), (3, 2), (4, 7), (5, 99), (6, 6)]
# for idx, ele in enum_lst:
#     print(idx, ele)

## parallel lists
## zip()
# lst1 = [4, 3, 99, 2, 7, 99, 6]
# lst2 = [4, 5, 22, 65, 7, 2, 1]
# lst3 = [7, 2, 1]
# for a, b, c in zip(lst1, lst2, lst3):
#     print( a, b, c )

# names = ["James", "Joanne", "Jessie"]
# ages  = [37     , 31      , 89]
# for name, age in zip(names, ages):
#     print(name, age)

## unpacking
# name, age = ("billy", 57)
#
# print(name, age)

####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
