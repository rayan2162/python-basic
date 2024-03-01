# copyfile() = copies contents of a file.
# copy() = copyfile() + permission mode + destination (can be a directory).
# copy() = copy() + copies metadata (file's creation and modification times).

import shutil,os

source = "file.txt"
destination = "Folder//copy.txt"

try:
    if os.path.exists(destination):
        print("Already copied!")
    else:
        shutil.copy(source,destination)
except FileNotFoundError:
    print(source + " not found!")