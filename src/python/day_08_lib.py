# """ un/comment to de/activate ###########################

## overview
# data types
    # int, float
    # bool
    # None
    # str

    # list
        # range

# abstractions
    # variables
    # functions

# control flow
    # if elif else
    # == != < > <= >=
    # not and or
    # el in list

# iteration
    # for

# review: checkin
    # range # <--------
        # start, stop, step

    # subscripting / indexing
    # slicing # <--------
    # checks for membership <---- quickly
    # concatination <---- quickly

# mutability


####################################################### """
""" un/comment to de/activate ###########################

# checks for membership
lst = [4, 5, 3, 8, 7, 8, 5, 9]
element = 5
print( element in lst )
print( 5 in lst )
print( element in [4, 5, 3, 8, 7, 8, 5, 9] )
print( 5 in [4, 5, 3, 8, 7, 8, 5, 9] )

# concatination
a = "hello"
b = a + " " + "world"
print(a)
print(b) # helloworld

lst1 = [4, 5, 3, 8]
print(lst1)
lst2 = lst1 + [7, 8, 5, 9]
print(lst1)
print(lst2)

####################################################### """
""" un/comment to de/activate ###########################

lst     = [4, 5, 3, 8, 7, 8, 5, 9]
print( lst )

sub_lst = lst[::]
print(  id( lst )  ) # different id...
print(  id( sub_lst )  ) # different id...

####################################################### """
""" un/comment to de/activate ###########################

start = 5
stop = 10
step = 1
for i in range(10, 5-1, -1):
    print(i)

# for 1 argument
# what must the type be
    # int
# what parameter name does that 1 argument coraspond too
    # stop
# what are the default values of the other 2 parameters
    # start = 0, step = 1

####################################################### """
""" un/comment to de/activate ###########################

intial_data = [1, 2]
test_data = intial_data.copy()

test_data.append(3)
print( id(test_data), test_data )
print( id(intial_data), intial_data )

####################################################### """
""" un/comment to de/activate ###########################

def my_function(lst):
    lst_copy = lst.copy()
    for num in lst:
        if num % 2 == 1:
            lst_copy.remove(num)

    return lst_copy


my_lst = [3, 4, 5]
print( my_lst)
print( my_function(my_lst) )
print( my_lst)

####################################################### """
""" un/comment to de/activate ###########################

lst = [4, 9, 8, 9]
for num in lst:
    print(num)

####################################################### """
""" un/comment to de/activate ###########################

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, ["hello", 85, True], 0]

# How would you index to get the value 8
print(x[7])

# How would you slice to get the list: [5, 3, 1]
print(x[4::-2])

# How would you replace the value 4 with the value 10 using indexing?
print(x[3])
x[3] = 10
print(x[3])
x[3] = 4

# How would you slice into the list to get: ["hello", 85]
print( x[9][:2:] )

# How would you add the value 42 to the list?
x.append(42)
print(x)

####################################################### """
""" un/comment to de/activate ###########################
'''
Given the following list of letters, create a function that goes through each letter and prints the letter if it is a vowel.

It will be helpful to write a helper function that returns True if a character is a vowel and call it within this function

Create a plan before coding
'''
def vowels(txt):
    lst = []
    for ch in txt:
        if ch in "aeiou":
            lst.append(ch)

    return lst


char_list = ['o', 'r', 'c', 'h', 'i', 'd']
print( vowels(char_list) )

####################################################### """
""" un/comment to de/activate ###########################

def sum_of_squares(iterable):
    total = 0
    for i in iterable:
        total += i**2

    return total

src = [4, 3, 6, 8, 2, 8, 7, 1]
# print( sum_of_squares(src) )


def sum_of_squares_in_range(n):
    total = 0
    for i in range(1, n+1):
        total += i**2

    return total


print( sum_of_squares_in_range(10) )

def sum_of_squares_in_range(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i**2)

    return sum(lst)

print( sum_of_squares_in_range(10) )


def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod


print(factorial(4))
print(factorial(5))

####################################################### """
""" un/comment to de/activate ###########################

counter = 0
for i in range(42):
    if i % 3 == 0:
        counter += 1

print(counter)

####################################################### """
# """ un/comment to de/activate ###########################

lst = [4, 5, 6, 4, 6, 2, 7]
for i in range( 10 ):
    for j in range( i+1, 10):
        print( slice(i, j, lst) )


####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
