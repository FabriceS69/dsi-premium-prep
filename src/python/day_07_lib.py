""" un/comment to de/activate ###########################

# overview
# data types
    # int, float
    # bool
    # str
    # None

    # list # main topic

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else
    # == != < > <= >=
    # not, and, or
    # in # for testing for membership

# iteration
    # for # main topic

####################################################### """
""" un/comment to de/activate ###########################

# recap: lists, for loops
lst = []
print(lst)
lst.append("hello")
print(lst)
lst.append(4)
print(lst)
lst.append(3)
print(lst)
lst.append(37)
print(lst)

####################################################### """
""" un/comment to de/activate ###########################

# recap: lists, for loops

nums = [5, 2, 8, 5, 6, 2]
for num in nums:
    print(num)

####################################################### """
""" un/comment to de/activate ###########################

# recap: lists, for loops

words = ["Whose", "woods", "these", "are", "I", "think", "I", "know"]
print( words )
# print( words[0] )
# print( words[-0] ) # same as 0
# print( words[1] )
# print( words[-1] )
# print( words[-2] )
# print( words[8] )  # IndexError: list index out of range
# print( words[-9] ) # IndexError: list index out of range

####################################################### """
""" un/comment to de/activate ###########################

# what is the difference between those two?
# nums = [5, 2, 8, 5, 6, 2]
# for num in nums:
#     print(num)

nums = [5, 2, 8, 5, 6, 2]
for num in range( len(nums) ):
    print( num )


####################################################### """
""" un/comment to de/activate ###########################

# ION # template for learning new functions
# Inputs
# Outputs
# Notes

# ION
# Inputs
    # 1
        # range implicitly starts at 0
        # stop <int>: defines the upper (stoping) bound of the range
            # the actual stop value passed is not included in the range generated, the range goes up to but not including the stop

    # 2
        # start <int>: defines the lower (starting) bound of the range
        # stop <int>: defines the upper (stoping) bound of the range

    # 3
        # start <int>: defines the lower (starting) bound of the range
        # stop <int>: defines the upper (stoping) bound of the range
        # step <int>: defines the interval (step) with which numbers will be added to the range

# Outputs
    # <range>: a generated range of numbers from `start` to `stop` (ex) in steps of `step`

# Notes
    # takes 1, 2 or 3 inputs
    # generates a "range" of numbers defined by it's inputs


# continue from lists "range function" section


# 1 argument
for i in range(5):
    print(i) # 0 -> 1 -> 2 -> 3 -> 4

# 2 arguments
n = 5
for i in range(1, n+1):
    print(i) # 1 -> 2 -> 3 -> 4 -> 5

# 3 arguments
n = 20
for i in range(1, n+1, 2):
    print(i) # 1 -> 2 -> 3 -> 4 -> 5

# cover slicing and start stop step + with range

# accumulator pattern

####################################################### """
""" un/comment to de/activate ###########################

n = 4
for i in range(n):
    print(i)

# n = 4.0
# for i in range(n): # TypeError: 'float' object cannot be interpreted as an integer
#     print(i)

n = 4.3
for i in range(int(n)):
    print(i)

####################################################### """
""" un/comment to de/activate ###########################

# start defaults to 0
# stop is always supplied
# step defaults to 1

# range(0, 20, 3)

####################################################### """
""" un/comment to de/activate ###########################

lst = [5, 2, 7, 6, 9]
print( 4 in lst ) # False
print( 5 in lst ) # True

print( 4 not in lst ) # True
print( 5 not in lst ) # False

# print( not 4 in lst ) # True
# print( not 5 in lst ) # False

####################################################### """
""" un/comment to de/activate ###########################

words   = ["Whose", "woods", "these", "are", "I", "think", "I", "know"]
goal    = ["woods", "these", "are", "I"]
sub_lst = words[1:4+1]
# sub_lst = words[1:4+1:]

print(sub_lst)

####################################################### """
""" un/comment to de/activate ###########################

lst_o_lsts = [[3, 5, 7], ["a", "b", "c"], [2.4, 3.9, 7.0]]
print( lst_o_lsts )
print( lst_o_lsts[1] )

print()
# print( lst_o_lsts[1][2] )
lst_o_lsts[1].append("hello")
print( lst_o_lsts )
print( lst_o_lsts[1] )

abc_lst = lst_o_lsts[1]
print(abc_lst)
abc_lst.append("world")
print(abc_lst)

####################################################### """
""" un/comment to de/activate ###########################

num_lst = list(range(4, 16))

print( num_lst )

# index num_list to get 6
print( num_lst[2] )
# index num_list to get 15
print( num_lst[-1] )
# slice num_list to get this sublist: [10, 11, 12, 13, 14, 15]
print( num_lst[6::] )
# slice num_list to get this sublist: [4, 6, 8, 10, 12, 14]
print( num_lst[::2] )
# slice num_list to get this sublist: [8, 7, 6, 5, 4]
print( num_lst[4::-1] )
print( num_lst[:5:][::-1] )

####################################################### """
""" un/comment to de/activate ###########################

num = 10
print( id(num), num) # 94139735322208 10
num += 10
print( id(num), num) # 94139735322528 20

a = 5
b = 3
c = a + b
print( a )
print( b )
print( c )

# lst = []
# print( id(lst), lst )
# lst.append("hello")
# print( id(lst), lst )

####################################################### """
""" un/comment to de/activate ###########################

a = 10
z = a
print( id(a), a )
print( id(z), z )
a += 1
print( id(a), a )
print( id(z), z )

####################################################### """
""" un/comment to de/activate ###########################

lst = []
print( id(lst), lst )
lst.append("hello")
print( id(lst), lst )

####################################################### """
# """ un/comment to de/activate ###########################



####################################################### """
