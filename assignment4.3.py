# Exercise 4.3: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

def display_student(name, age):
    print(name, age)

display_student("Sam", 21)
showStudent = display_student
showStudent("Sam", 21)
