s1 = {1,2,3,4,5,6,7}
s2 = {4,5,6,7,8,9,10}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

print(s1)
print(s2);

s1.intersection_update(s2)
print(s1)

s3 = {1,2,3,4,5,6,7,8,9,10}

s4 = {4,5,6}

print(s4.issubset(s3))
print(s3.issuperset(s4))