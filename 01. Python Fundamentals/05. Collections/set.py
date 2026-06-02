s1 = {4,5,6,63,23,6,2,36,7,23,5}
print(s1)
print(type(s1))

s2 = {"abcd",'hello',56246,63.34,True}
print(s2)

l1 = [1,265,73,3,3,3,3,3,63,63,63,46,7,34]
t1 = (5,73,423,623,73,73,73)

l1 = set(l1)
print(l1)


for ele in s1:
    print(ele)

s2.add(67)
s2.add(67)
print(s2)


s1.update(l1)
print(s1)

s1.remove(265)
print(s1)

s1.discard(46)
print(s1)

print(s1.pop())
print(s1.pop())
print(s1)