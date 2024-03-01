# L = local
# E = Enclosing
# G = Global
# B = Build-in

name = "Global"

def display():
    name = "Local"
    print(name)

def display2():
    print(name)

print(name)
display()
display2()