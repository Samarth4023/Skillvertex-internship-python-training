# Exercise 3.4: Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34

nterms = 10
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
