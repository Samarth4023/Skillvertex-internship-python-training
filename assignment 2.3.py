# Exercise 2.3: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.If numbers are different then return False.

a = [10, 20, 30, 40, 10]
b = [10, 20, 30, 40, 50]
if a[0] == a[-1]:
    print("Given list is",a, "\n\tResult is True\nHence, fist and last number are same")
else:
    print("Given list is",a, "\n\tResult is False\nHence, fist and last number are not same")
if b[0] == b[-1]:
    print("Given list is",b, "\n\tResult is True\nHence, fist and last number are same")
else:
    print("Given list is",b, "\n\tResult is False\nHence, fist and last number are not same")
