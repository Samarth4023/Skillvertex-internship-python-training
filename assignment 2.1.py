# Exercise 2.1: Print characters from a string that are present at an even index number 
# Write a program to accept a string from the user and display characters that are present at an even index number. 
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

x = input("Enter the word ")
list = []
for i in range(0,len(x)):
    if i % 2 == 0:
        list.append(x[i])
print(list)
