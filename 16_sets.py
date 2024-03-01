# set = is a collection which is unordered, unindexed, NO duplicate value

utensils = {"fork", "spoon", "knife"}

for i in utensils:
    print(i)

utensils.add("napkin")
print(utensils)

utensils.remove("napkin")
print(utensils)

dishes = {"bowl", "plate", "cup","knife"}

print(utensils.difference(dishes))
print(dishes.difference(utensils))

utensils.update(dishes)
print(utensils)
print(dishes)


# join two sets to create a new set
dinner_table = dishes.union(utensils)
print(dinner_table)

print(utensils.intersection(dishes))
