# for standard python library
import os

source = "source_file.txt"
destination = "Folder//source_file.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print("successfully replaced")
except FileNotFoundError:
    print(source + " was not found.")