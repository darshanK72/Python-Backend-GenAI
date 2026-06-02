l = [1,2,3,4,5]
print(type(l))

t1 = (1,2,3,4,5)
print(type(t1))

# Indexing

t2 = (52,62,62,13267,3,45,2,47,452,6346,356,235,3,634,6)
print(t2[7])
print(t2[-2])

# Tuple is Immutable - cannot change
# t2[1] = 6364

print(t2)

print(t2[3:9:2])

for i in range(len(t2)):
    print(t2[i],end=" ")

print()

for ele in t2:
    print(ele,end=" ")

print()

print(t2.count(3))
print(t2.index(13267))


t3 = (1,2,3)
print(t3)
print(type(t3))
t3 = list(t3)
print(t3)
print(type(t3))

t3[1] = 6000

print(t3)

t3 = tuple(t3)
print(t3)
print(type(t3))

t4 = (5,7,2)
t4 = list(t4)
t4[0] = 500
t4 = tuple(t4)
print(t4)