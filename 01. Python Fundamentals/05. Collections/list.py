# 1. String 
# 2. List
# 3. Tuple
# 4. Set
# 5. Dictionary

l = [4,52,25,3,62,3534]
# print(l)
# print(type(l))

l1 = [1,42,523,5235,56.354,34.23,63.34,"hello","apple",True,False,(3+4j),[76,634]]
# print(l1)
# print(type(l))

# Positive Indexing
print(l1[7])
print(l1[0])

# Negative Indexing
print(l1[-3])

l1[0] = 1000;

# Slicing
print(l1[:5])
print(l1[3:9])
print(l1[2:10:2])
print(l1[::-1])


for i in range(len(l1)):
    print(l1[i],end=" ")

print()

for ele in l1:
    print(ele,end=" ")

print(l*2)