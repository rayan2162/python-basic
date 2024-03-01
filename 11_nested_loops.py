rows = int(input("How many rows "))
column = int(input("How many columns? "))
symbol= input("Enter the symbol to print : ")

for i in range(0,rows,1):
    for j in range(0, column,1):
        print(symbol,end="")
    print()