# Exercise 4.1: Create a function with variable length of arguments
# Write a program to create a function funcN() to accept a variable length of arguments and print their value.

def funcN(*args):
    for i in args:
        print(i)

funcN(10, 20, 30)
funcN(40, 50)
