# Exercise 3.2: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number


def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
n = int(input("Enter the number: "))
print("Sum of all given numbers are: ")
print( getSum(n))
