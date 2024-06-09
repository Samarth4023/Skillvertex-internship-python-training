# Exercise 2.2: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

a = input("Enter a string: ")
n = int(input("Enter a number: "))
if n < len(a):
    print(a[n:])
else:
    print("Error- Number should be smaller than the length of the string")
