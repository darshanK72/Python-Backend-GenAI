
# int add(int a,int b)
# {
#     return a + b;
# }

def add(a,b):
    return a + b

# n! = 1*2*3*--n 
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f


print(add(20,50))

print(factorial(5))