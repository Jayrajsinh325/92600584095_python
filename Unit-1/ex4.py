#4. write a program to demonsrtate string oprations including slicing formatting and built-in srting functions.

print("Slicing:")
text="Pyhon Programming"

print(f"First 6 characters:",{text[:6]})
print(f"Slicing from 3 to 12 characters:",{text[3:12]})
print(f"Slicing from even characters:",{text[::2]})


print("Built-in Functions:")

print("Upper Case:",text.upper())
print("Lower Case:",text.lower())
print("Find Characters:",text.find("Programming"))

