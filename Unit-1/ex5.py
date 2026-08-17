# 5.Write a program to create and manipulate lists  using indexing slicing and list comprehensions.

a = [10, 20, 30, 40, 50]

print("List =", a)

print("First element =", a[0])
print("Last element =", a[-1])

print("Slicing =", a[1:4])

a.append(90)
print("After append =", a)

a.remove(30)
print("After remove =", a)

# List comprehension
b = [x * 2 for x in a]

print("List comprehension =", b)