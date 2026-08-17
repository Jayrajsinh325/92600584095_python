# 6.Write a program to illustrate the use of tuples  and sets with basic operations.


t = (10, 20, 30, 40)

print("Tuple =", t)
print("First element =", t[0])
print("Tuple length =", len(t))


s = {10, 20, 30, 40}

print("Set =", s)

s.add(50)
print("After add =", s)

s.remove(20)
print("After remove =", s)

s1 = {10, 20, 30}
s2 = {20, 30, 40}

print("Union =", s1 | s2)
print("Intersection =", s1 & s2)