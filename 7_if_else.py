age = input("How old are you? ")

if int(age)>=18:
    print("You are adult")

elif int(age)<18 and int(age)>0:
    print("You aren't an adult")

else:
    print("You haven't been born")