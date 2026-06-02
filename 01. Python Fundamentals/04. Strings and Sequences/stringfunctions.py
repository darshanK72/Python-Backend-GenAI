s1 = "hello world this Is FIRST string"
print(s1)
print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())

s2 = "abcdAGASDF"
print(s2.isalpha())

s3 = "55234534"
print(s3.isdigit())

s4 = "asdfasdf532523"
print(s4.isalnum())


s5 = "hello this is sparta, is is is to world welcome welcome to world"
print(s5.find("sparta"))
print(s5.index("sparta"))
print(s5.count("is"))

s6 = "          asdfasdfasdf         "
print(s6.lstrip())
print(s6.rstrip())
print(s6.strip())

s7 = "$$$$$$$$$$$$asdfasdfasdf$$$$$$$$$$$$$$$"
print(s7.lstrip("$"))
print(s7.rstrip("$"))
print(s7.strip("$"))

print(s5.split())

s8 = "hello-world-this-sparta"
print(s8.split("-"))

l1 = ['hello', 'world', 'this', 'sparta']

print("%".join(l1))

name = "Ravi"
age = 21
marks = 702.23

print("name of student is {} and age is {} and marks is {}".format(name,age,marks))
print("name of student is {2} and age is {1} and marks is {0}".format(marks,age,name))


# F-string 
print(f"name of student is {name} and age is {age} and marks is {marks}")


