# break = terminate loop
# continue = skips to next iteration
# pass = does nothing act as a placeholder

while True:
    name = input("Enter your name : ")
    if name !="":
        break

phone = "123-456-789"
for i in phone:
    if i == "-":
        continue
    else:
        print(i,end="")
print()

for j in phone:
    if j == "-":
        pass
    else:
        print(j,end="")
print()