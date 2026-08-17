# 9.Write a program to define and use user-defined  functions with different types of arguments. 

# No argument
def hello():
    print("Hello Python")

hello()

# Positional arguments
def add(a, b):
    print("Addition =", a + b)

add(10, 20)

# Default argument
def greet(name="Student"):
    print("Hello", name)

greet()
greet("jayrajsinh")

# Keyword arguments
def student(name, age):
    print("Name =", name)
    print("Age =", age)

student(age=23, name="jayrajsinh")