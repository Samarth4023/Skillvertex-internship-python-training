# Exercise 3.3: Print list in reverse order using a loop
# I/P: List1 = [10, 20, 30, 40, 50]
# O/P: 50 40 30 20 10

List1 = [10, 20, 30, 40, 50]
for i in range(len(List1)-1, -1, -1):
    print(List1[i], end=" ")
    