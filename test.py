s = input()
r = len(s)
for i in range(0,r):
    if s[i]>='a' and s[i]<='z':
        print(s[i].upper() , end="")
    if s[i]>='A' and s[i]<='Z':
        print(s[i].lower(), end="")