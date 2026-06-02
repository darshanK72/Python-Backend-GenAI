l1 = []

for i in range(1001):
  if i % 2 == 0:
    l1.append(i)

print(l1)

d1 = {}

for i in range(1,101):
  d1[i] = i*i

print(d1)

l2 = [i for i in range(1001) if i % 2 == 0]
print(l2)

d2 = {i:i*i for i in range(1,101)}
print(d2)

l3 = [10,20,30,40,50]
for i,j in enumerate(l3):
  print(i,":",j)

