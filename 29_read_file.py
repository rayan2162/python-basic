''' 
main code ->
    with open('file.txt') as file:
        print(file.read())

automatically closes file because of with open()
'''

try:
    with open('file.txt','r') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")