# """ un/comment to de/activate ###########################

# overview
# data types
    # int, float
    # bool
    # str
    # None

    # list

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else

# iteration / repetition
    # for
    # while

####################################################### """
""" un/comment to de/activate ###########################

def some_function(x):
    if x % 2 == 0 and x % 5 == 0:
        return 'Gimme 10!'
    elif x % 5 == 0:
        return 'High Five!'
    elif x % 2 == 0:
        return 'Evens!'
    else:
        return 'I got nothing'


x = 9
print( some_function(x) ) # I got nothing
x = 80
print( some_function(x) ) # Gimme 10!
x = 25
print( some_function(x) ) # High Five!
x = 66
print( some_function(x) ) # Evens!

####################################################### """
""" un/comment to de/activate ###########################

def add_nums(a, b):
    return a + b


eleven = add_nums(3, 8)
print( "the value of the variable eleven is:", eleven )

# print( eleven + 9 )

####################################################### """
""" un/comment to de/activate ###########################

# SyntaxError: non-default argument follows default argument
# def add_nums(a=1, b):

def add_nums(a, b=1):
    return a + b

print( add_nums(15) )
# print( add_nums() )

####################################################### """
""" un/comment to de/activate ###########################

lst = [4, 6, 7, 2, 24, 5]
print( lst[4] )

####################################################### """
""" un/comment to de/activate ###########################

lst = []
print(lst)
lst.append(4)
print(lst)

####################################################### """
""" un/comment to de/activate ###########################

def squares_lst(src_lst):
    lst = []
    for num in src_lst:
        lst.append(num**2)

    return lst


some_lst = [5, 6, 2, 7, 9, 15, 27, -3, 3]
print( squares_lst(some_lst) )

####################################################### """
""" un/comment to de/activate ###########################

some_lst = [5, 6, 2, 7, 9, 15, 27, -3, 3]
# print(some_lst)
# print(len(some_lst))
for i in range(len(some_lst)):
    element = some_lst[i]
    print(element)
    print(i)

####################################################### """
""" un/comment to de/activate ###########################

def squares_lst(src_lst):
    lst = []
    for i in range(len(src_lst)):
        lst.append( src_lst[i]**2 )

    return lst


some_lst = [5, 6, 2, 7, 9, 15, 27, -3, 3]
print( squares_lst(some_lst) )

####################################################### """
""" un/comment to de/activate ###########################

some_lst = [5, 6, 2, 7, 9, 15, 27, -3, 3]
count = 0
for _ in some_lst:
    count += 1

print(count)

####################################################### """
""" un/comment to de/activate ###########################
# looping through indexed collections (list, str, tuple ...)

# elements are extracted
src_lst = [44, 22, 77]
for ele in src_lst:
    print(ele)


# indicies are "modeled"
src_lst = [44, 22, 77]
for idx in range( len(src_lst) ):
    print(idx)

####################################################### """
