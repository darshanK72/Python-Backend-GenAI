try:
    a = int(input("Enter Number : "))
    b = int(input("Enter Number : "))
    if(a < b):
        raise 20
    print(a / b)
except ZeroDivisionError as e:
    print(e)
except NameError:
    print("Name Error happend")
except ValueError:
    print("Value Error happend")
except:
    print("Other error happened")
finally:
    print("Finaly this is done")