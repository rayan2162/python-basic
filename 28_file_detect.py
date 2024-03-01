import os

path = "//home//rayan//Desktop//F//python//file.txt"

path2 = "Folder"

if os.path.exists(path):
    print("That location exists")
else:
    print("That location doesn't exist")

if os.path.isfile(path2):
        print("That is a file")
else:
    print("Thats a folder")

if os.path.isdir(path):
    print("This is a directory")