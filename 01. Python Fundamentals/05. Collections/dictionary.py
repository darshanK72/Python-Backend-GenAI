
d1 = {"one":1,"two":2,"three":3}
print(d1)
print(type(d1))

d2 = {
    "name":"Ravi Sharma",
    "age":22,
    "marks":78.23,
    "div":"E"
}

l1 = [2,5,62,6]
print(l1[1])

print(d2["name"])

print(d2.get("name"))

print(d2["marks"])

print(len(d2))

d2["address"] = "Nashik"

print(d2)

d2.update({"school":"K.B.H Vidilaya"})

print(d2)

d2.pop("school")

print(d2)

for ele in d2:
  print(d2[ele])

for k,v in d2.items():
  print(k ,":",v)

print(d2.keys())

for k in d2.keys():
  print(k)

for v in d2.values():
  print(v)

d2.popitem()

print(d2)

