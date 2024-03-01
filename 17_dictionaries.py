# dictionary = a changeable, unordered collection of unique key:value pairs. 
# Fast because they use hashing.

capitals = {"USA":"Washington DC",
            "Chaina":"Beijing",
            "Bangladesh":"Dhaka",
            "Russia":"Moscow"}

print(capitals["Bangladesh"])

print(capitals.get("Germany"))

capitals.update({"Germany":"Berlin"})

capitals.update({"USA":"WDC"})

print(capitals.keys())
print(capitals.values())
print(capitals.items())


capitals.pop("USA")

for key,value in capitals.items():
    print(key,value)

print(capitals.clear())
for key,value in capitals.items():
    print(key,value)