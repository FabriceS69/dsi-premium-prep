
# """ un/comment to de/activate ###########################

## overview
# data types
    # int, float
    # bool
    # None
    # str "" ''

# abstractions
    # variables
    # functions

# control flow
    # dynamic code

# iteration
    # repete operations

####################################################### """
""" un/comment to de/activate ###########################

# if condition:
    # consequent

a = 7
b = 50

# print( a > b )
if a > b: # IndentationError: expected an indented block
    print( "a is greater than b" )
    # print( "this is the conseqent of first condition" )
elif b > a:
    print( "b is greater than a" )
else:
    print( "a and b are equal" )


print("fin")

    # print( "what will happen" ) # IndentationError: unexpected indent





####################################################### """
""" un/comment to de/activate ###########################

# a is greater than b
a = 7
b = 5

if a > b: # <- this condition is True
    print( "a is greater than b" )
elif b > a:
    print( "b is greater than a" )
else:
    print( "a and b are equal" )



# b is greater than a
a = 7
b = 50

if a > b:
    print( "a is greater than b" )
elif b > a: # <- this condition is True
    print( "b is greater than a" )
else:
    print( "a and b are equal" )



# a and b are equal
a = 50
b = 50

if a > b:
    print( "a is greater than b" )
elif b > a:
    print( "b is greater than a" )
else: # <- all prior conditions were False
    print( "a and b are equal" )



####################################################### """
""" un/comment to de/activate ###########################

# n = 75
# if n > 10:
#     print("n > 10")
# elif n > 30:
#     print("n > 30")

n = 75
if n > 10:
    print("n > 10")
if n > 30:
    print("n > 30")

'''
n > 10
n > 30
'''


####################################################### """
""" un/comment to de/activate ###########################


n = 40
if n > 30:
    print("n > 10")
    print("n > 30")
elif n > 10:
    print("n > 10")

'''
n > 10
n > 30
'''


####################################################### """
""" un/comment to de/activate ###########################

n = 75
if n > 10:
    print("n > 10")
if n > 20:
    print("n > 20")
if n > 30:
    print("n > 30")
if n > 40:
    print("n > 40")
if n > 50:
    print("n > 50")
if n > 60:
    print("n > 60")
if n > 70:
    print("n > 70")
if n > 80:
    print("n > 80")
if n > 90:
    print("n > 90")
if n > 100:
    print("n > 100")

####################################################### """
""" un/comment to de/activate ###########################

n = 30
if n > 100:
    print("n > 100")
elif n > 90:
    print("n > 90")
elif n > 80:
    print("n > 80")
elif n > 70:
    print("n > 70")
elif n > 60:
    print("n > 60")
elif n > 50:
    print("n > 50")
elif n > 40:
    print("n > 40")
elif n > 30:
    print("n > 30")
elif n > 20:
    print("n > 20")
elif n > 10:
    print("n > 10")
else:
    print("n > 0")

####################################################### """
""" un/comment to de/activate ###########################

a = 7
b = 50
if not a > b:
    print("b is greater than or equal to a")

####################################################### """
""" un/comment to de/activate ###########################

# True  and True  -> True
# True  and False -> False
# False and True  -> False
# False and False -> False

# True  or True  -> True
# True  or False -> True
# False or True  -> True
# False or False -> False

# not True -> False
# not False -> True

# PNAO
# 1
(
    not (
        not (True or False) and (True and True)
    )
) and True or True

# 2
(
    not (
        not (True or False) and True
    )
) and True or True

# 3
(
    not (
        not True and True
    )
) and True or True

# 4
(
    not (
        False and True
    )
) and True or True

# 5
(
    not (
        False
    )
) and True or True

# 6
(
    True
) and True or True

# 7
True

####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
