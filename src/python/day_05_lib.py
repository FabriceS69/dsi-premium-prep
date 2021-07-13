""" un/comment to de/activate ###########################

# overview
# data types
    # int / float
    # bool
    # str
    # None

# abstractions
    # variables
    # functions <- todays main topic

# control flow
    # if, elif, else

# iteration
    # for
    # while

# recap: control flow

a = 10
b = 7

if a > b:
    print("a is greater than b")
elif b > a:
    print("a is less than b")
else:
    print("a is equal to b")

####################################################### """
""" un/comment to de/activate ###########################

n = 77

# print ALL statements that are True
if n > 10:
    print("n is greater than 10")
if n > 20:
    print("n is greater than 20")
if n > 30:
    print("n is greater than 30")
if n > 40:
    print("n is greater than 40")
if n > 50:
    print("n is greater than 50")
if n > 60:
    print("n is greater than 60")
if n > 70:
    print("n is greater than 70")
if n > 80:
    print("n is greater than 80")
if n > 90:
    print("n is greater than 90")
if n > 100:
    print("n is greater than 100")

####################################################### """
""" un/comment to de/activate ###########################

n = 77

# print ONLY THE LARGEST SINGLE statement that are True
if n > 100:
    print("n is greater than 100")
elif n > 90:
    print("n is greater than 90")
elif n > 80:
    print("n is greater than 80")
elif n > 70:
    print("n is greater than 70")
elif n > 60:
    print("n is greater than 60")
elif n > 50:
    print("n is greater than 50")
elif n > 40:
    print("n is greater than 40")
elif n > 30:
    print("n is greater than 30")
elif n > 20:
    print("n is greater than 20")
elif n > 10:
    print("n is greater than 10")

####################################################### """
""" un/comment to de/activate ###########################

# phases of a function
# definition
# invocation (call)

####################################################### """
""" un/comment to de/activate ###########################

# phases of a function
# definition
def factorial(n):
    print("the value of n is", n)
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod

# invocation (call)
print( factorial(4) ) # 24
print( factorial(5) ) # 120

print("fin")

####################################################### """
""" un/comment to de/activate ###########################

# def -> function_name -> (parameter_1, parameter_2) -> :
    # ...

'''
take in a number
return that number plus 10
'''

def add_10(n):
    return n + 10

print( add_10(20) )

'''
discription:
    `double` takes a number and returns a number that is twice the value of the input

inputs:
    n <num>: the number that the double is calculated against

return:
    <num>: a number which is twice the value of n
'''

def double(n):
    return n * 2


print( double(3) ) # 6
print( double(5) ) # 10
print( double(12) ) # 24

####################################################### """
""" un/comment to de/activate ###########################

def addition(a, b):
    return a + b

print( addition(7, 8) ) # 15


####################################################### """
""" un/comment to de/activate ###########################

def subtraction(a, b): # a and b are parameters
    return a - b


print( subtraction(10, 6) ) # 4 # 10 and 6 are arguments
print( subtraction(6, 10) ) # -4

# "parameters"
# "arguments"
    # "passing" arguments to a function


####################################################### """
""" un/comment to de/activate ###########################

def subtraction(a, b):
    return a - b


# print( subtraction ) # <function subtraction at 0x7f04741a2c10>

# print( subtraction() )
# TypeError: subtraction() missing 2 required positional arguments: 'a' and 'b'

# print( subtraction(10) )
# TypeError: subtraction() missing 1 required positional arguments: 'a' and 'b'

print( subtraction(10, 6) ) # 4 # works fine

# print( subtraction(10, 6, 4) )
# TypeError: subtraction() takes 2 positional arguments but 3 were given

####################################################### """
""" un/comment to de/activate ###########################

n = 77

# print ALL statements that are True
if n > 10:
    print("n is greater than 10")
if n > 20:
    print("n is greater than 20")
if n > 30:
    print("n is greater than 30")
if n > 40:
    print("n is greater than 40")
if n > 50:
    print("n is greater than 50")
if n > 60:
    print("n is greater than 60")
if n > 70:
    print("n is greater than 70")
if n > 80:
    print("n is greater than 80")
if n > 90:
    print("n is greater than 90")
if n > 100:
    print("n is greater than 100")


n = 42

# print ONLY THE LARGEST SINGLE statement that are True
if n > 100:
    print("n is greater than 100")
elif n > 90:
    print("n is greater than 90")
elif n > 80:
    print("n is greater than 80")
elif n > 70:
    print("n is greater than 70")
elif n > 60:
    print("n is greater than 60")
elif n > 50:
    print("n is greater than 50")
elif n > 40:
    print("n is greater than 40")
elif n > 30:
    print("n is greater than 30")
elif n > 20:
    print("n is greater than 20")
elif n > 10:
    print("n is greater than 10")


# reversed the order
# changed ifs to elifs


# if first condition == True:
#     first consequent
# elif second condition:
#     second consequent

####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
