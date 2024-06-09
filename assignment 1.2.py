# Exercise 1.2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number

print("======================================================================")
print("Printing the sum of current and previous number in a given range(10)")
print("======================================================================")
for i in range(10):
    print("Current number: ", i, "\tPrevious Number: ", i-1, "\nSum = ", (i*2)-1)
