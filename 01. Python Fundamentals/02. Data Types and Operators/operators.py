
a = 52
b = 14

print("sum =",a + b)
print("sub =",a - b)
print("mul =",a * b)
print("div =",a / b)
print("mod =",a % b)
print("floor div =",a // b)
print("exp =",4 ** 2)


x = 20
print("x =",x)
x += 5
print("x =",x)
x -= 10
print("x =",x)
x *= 3
print("x =",x)


print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


c = 67

ra = (a > b) and (a > c)
rb = (b > a) and (b > c)
rc = (c > a) and (c > b)

print("ra =",ra)
print("rb =",rb)
print("rc =",rc)


p = 40
q = 40

print(p is q)
print(p is not q)

s1 = "hello world, this is sparta"
s2 = "thisasdfa"

print(s2 in s1)
print(s2 not in s1)