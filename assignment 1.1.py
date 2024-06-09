# Exercise 1.1: Calculate the multiplication and sum of two numbers 
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def func(n1, n2):
    if  n1 * n2 <= 1000:
        return( n1 * n2)
    else:
       return( n1 + n2)
#Case1:
print(func(40,20))
#CASE2:
print(func(60,30))
