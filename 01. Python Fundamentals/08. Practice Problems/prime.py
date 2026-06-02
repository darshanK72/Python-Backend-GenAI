n = int(input("Enter Number : "))
f = True

for i in range(2,n):
    if n % i == 0:
        f = False
        break


if f == True:
    print("Prime Number")
else:
    print("Not Prime Number")
