# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:44:51 2016

@author: Andrew
"""

# Whitespace Formatting
# Page 16

for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print("done looping")


# Exceptions
# Page 19

try:
    print(0/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# Lists
# Page 20
    
x = list(range(10)) # Everything else works as intended past this point

#Object-Oriented Programming
# Page 31

print(s.contains(4))
print(s.contains(3))

# Functional Tools
# Page 32

print(two_to_the(3))