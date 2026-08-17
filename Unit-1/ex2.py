#2. write a program to illusrtate thr use of different data types and type casting.

n=int(input("Enter the Integar number here:"))
typing=float(n)
retype=int(typing)

print(f"Original input is:{n}",type(n))

print(f"Converted into Float:{typing}",type(typing))

print(f"Converted into Integer:{retype}",type(retype))
