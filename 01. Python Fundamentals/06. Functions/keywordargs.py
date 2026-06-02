def display(a,b,c):
    print("a =",a)
    print("b =",b)
    print("c =",c)


display(c=2,a=6,b=22)


def show(**d):
    # for k,v in d.items():
    #     print(k,":",v)
    print(d)
    

show(c=2,a=6,b=22)