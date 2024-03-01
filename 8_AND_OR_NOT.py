temperature = input("What is the temperature outside? ")
temperature = int(temperature)

if temperature>=15 and temperature<=28:
    print("The weather is good")

elif (temperature>=5 and temperature <15) or (temperature>28 and temperature<=37):
    print("The weather isn't good")

elif (temperature<5 or temperature>40):
    print("Catastrophy!")
