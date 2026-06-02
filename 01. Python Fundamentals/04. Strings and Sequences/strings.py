s1 = "Hello it's World"
print(s1)

s2 = 'This is "new" statement'
print(s2)

s3 = """hello this is new world
asdfasdfadf
asdfasdf
hello
asdfasdf"""
print(s3)

# Positive Indexing
print(s1[7])
print(s1[0])
print(s2[9])

# Immutable - cannot change
# Mutable - can change 
# s1[11] = "M";

# Negative Indexing
print(s1[-1])
print(s1[-2])

# Slicing
print(s1[6:10])
print(s2[3:11])
print(s1[4:])
print(s1[:8])
print(s1[:])
print(s1[:11:2])

print(s1[-8:-2])

# Reverse String
print(s1[::-1])

# Length - len()
print(len(s1))

for i in range(len(s1)):
    print(s1[i])

for i in s1:
    print(i)