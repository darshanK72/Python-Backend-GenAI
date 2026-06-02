l1 = [5,252,23,73,4,36,6,35,36,3,563]
print(l1)

l1.append(700)

l2 = [76,703,23,6]

print(l1)

l1.extend(l2)

print(l1)

print(l1.index(35))

print(l1.count(36))

l2.clear()

print(l2)

l3 = l1.copy()
print(l3)


l1.insert(2,"Banana")

print(l1)

print(l1.pop())

print(l1)

l1.remove('Banana')

print(l1)

l1.sort()

print(l1)

l1.reverse()

print(l1)