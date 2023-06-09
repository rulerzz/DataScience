# VARIABLES In Python, variables are created when you assign a value to it
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 5
x = "String"
y = "Hello, World!"

print(x)
print(y)

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes

x = "John"
# is the same as
x = 'John'

# Case-Sensitive
# Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a

"""
Variable Names
    A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
# EXAMPLE
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# ASSIGNMENT
# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #apple
print(y) #banana
print(z) #cherry

"""Global Variables
    Variables that are created outside of a function (as in all of the examples above) are known as global variables.
    Global variables can be used by everyone, both inside of functions and outside
"""

x = "awesome" # X IS GLOBAL

def myfunc():
    print("Python is " + x)

myfunc() #Python is awesome

#LOCAL VARIABLES

x = "awesome"

def myfunc():
    x = "fantastic" #LOCAL VARIABLE
    print("Python is " + x) #Python is fantastic

myfunc()

print("Python is " + x) #Python is awesome

"""
The global Keyword
    Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
    To create a global variable inside a function, you can use the global keyword.
    To change the value of a global variable inside a function, refer to the variable by using the global keyword:
"""
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic
