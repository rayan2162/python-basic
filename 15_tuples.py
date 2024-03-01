# tuple = collection which is ordered and unchangeable used to group together related data
student = ("rayan", 21, "male")

print(student.count("rayan"))
print(student.index("male"))

for i in student:
    print(i, end=" ")

if "rayan" in student:
    print("yes")