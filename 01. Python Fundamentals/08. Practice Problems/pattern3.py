n = int(input("Enter Number :"))

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()