# Basics of Python Functions
* Function Parameters
* Printing vs Return
* Global vs Local Scope


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# More Quick Notes on Slack Etiquette
* Comment on the appropriate thread/channel, if possible, rather than sending a message out to the whole group
* Use three backticks to create a code block

```
# put your code within triple ticks to render them
#   as text editor text
```

* Use a single backtick on either side of some text to create an inline block, helpful for function names, operations, etc:
    * `some_function()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (2 minutes)
* What are the 4 scalar types we briefly discussed?
* What does `print(1/100**100000)` give us and why?
* What does `3 == 3` evaluate to?
* What does `2 != 2` evaluate to?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
* What are the 4 scalar types we briefly discussed?
    * `int, float, bool, str`
* What does `print(1/100**100000)` give us and why?
    * `0`, because the value is too small to represent with a `float`
* What does `3 == 3`  evaluate to? 
    * `True`
* What does `2 != 2` evaluate to?
    * `False`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
* What response will this code produce when:
    * `x = 9` 
    * `x = 80` 
    * `x = 25` 
    * `x = 66`

```python
if x % 5 == 0:
    print(‘High Five!’)
elif x % 2 == 0 and x % 5 == 0:
    print(‘Gimme 10!’)
elif x % 2 == 0:
    print(‘Evens!’)
else:
    print(“I got nothing”)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

* What response will this code produce when:
    * `x = 9` 
        * `I got nothing`
    * `x = 80` 
        * `High Five!`
    * `x = 25` 
        * `High Five!`
    * `x = 66`
        * `Evens!`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Using print() to output to console
* `print()`
    * function takes the value passed into it and writes that value to the console.
* `print()` is in your core toolset for checking what you expect is happening in your code.
* **the `print()` function is fundamentally different from the `return` keyword!**

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Functions
* Functions can be thought of as ways to create repeatable procedures
    * Name the function, give it parameters (optional), write your code
* Things we need to consider when making a functions:
    * How to name the function
    * What the function expects to pass into it - arguments
    * What the function does
    * What the function returns: a value or None?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Functions Basic Structure

```python
def my_func(arg1):
    # some block of code here
    return arg1 # Returns the value in arg1 when function is called
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Function **Parameters**
* Function parameters:
    * Function inputs that are inside the parentheses of the function header
    * Operate similar to variables but they only exist within the function

```python
def some_func(im_a_function_parameter): 
   return bool(im_a_function_parameter) 
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Function **Arguments**

* Pass in “arguments” to the parameters when the function is called.

```python
def add_one_to_num(num):
    return num + 1

x = 7

print(add_one_to_num(x)) # outputs 8 to console
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Default Arguments

* Default Arguments can be defined for function parameters. They are created in the function definition

```python
def add_two_numbers(num_1=1, num_2=2):
    return num_1 + num_2

print(add_two_numbers()) # outputs 3 to the console
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `print()` and `return` ARE DIFFERENT!!
* `print()` outputs to the console
* `return` defines the value that will be received from the scope of the function

```python
def some_func(x):
    print(x)

# is fundamentally different from
def another_func(x):
    return x
```














Bonus function: input()
The input() function accepts character input from the keyboard and prints the message it is passed as a prompt.