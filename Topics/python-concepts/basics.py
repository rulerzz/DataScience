
# COMMENTS BEGIN WITH A HASH

"""
MULTI LINE COMMENTS START WITH 3QUOTES
"""

# BASIC PRINT TO STDOUT
print("Hello, World!")
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #Python is awesome

x = 5
y = 10
print(x + y) #15

x = 5
y = "John"
print(x + y) #ERROR

x = 5
y = "John"
print(x , y) #PRINTS BOTH VALUES 5 John

"""
Python Indentation
Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code. Ex...
"""

if 5 > 2:
    print("Five is greater than two!") #---OK

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

if 5 > 2:
print("Five is greater than two!") #---SYNTAX ERROR

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error

if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!") #---SYNTAX ERROR MUST BE IN SAME BLOCK


