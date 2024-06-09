# Exercise 2.4: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

list = [29,30,32,22,45,35,67,40,83,65,63,24,73,48,39,34]
print("=========================================================================")
print("\tFrom the given list, numbers that are divisible by 5 are: ")
for num in list:
    if num % 5 != 0:
        continue
    else:
        print("\n", num)
