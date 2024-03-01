food = ["Pizza","Burger","French Fries","Coke"]
print(food)
food[3]="Sushi"
print(food)

for i in food:
    print(i)

# append adds at last
food.append("Ice Cream")
print(food)

food.remove("Burger")
print(food)

#pop removes last element
food.pop()
print(food)

food.insert(2,"Shake")
print(food)

food.sort()
print(food)

food.clear()
print(food)