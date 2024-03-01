# {} format fields acts as a placeholder

animal = "cow"
item = "moon"

print("The {1} jumped over the {0}".format(item,animal))

# keyword argument
print("The {animal} jumped over the {item}".format(animal="quick brown fox",item="lazy dog"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

#padding
name = "Rayan"

print("Hello, my name is {}. Nice to meet you".format(name))
#gives 10 place padding on right
print("Hello, my name is {:10}. Nice to meet you".format(name))
#gives 10 place padding on right
print("Hello, my name is {:<10}. Nice to meet you".format(name))
#gives 10 place padding on left
print("Hello, my name is {:>10}. Nice to meet you".format(name))
#gives 5/5 place paddingand text on center
print("Hello, my name is {:^10}. Nice to meet you".format(name))

pi = 3.14159
number = 1000

#floting point number formatting
print("The number pi is {:.2f}".format(pi))
#comma
print("The number is {:,}".format(number))
#octal
print("The number is {:o}".format(number))
#hexadecimal
print("The number is {:x}".format(number))
print("The number is {:X}".format(number))
#scientefic
print("The number is {:e}".format(number))
print("The number is {:E}".format(number))
