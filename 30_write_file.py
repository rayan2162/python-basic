text = "uh oh! \nThis test file is overwritten\n"

with open('file.txt','w') as file:
    file.write(text)

# a for append
new_text = "This is a new line added"
with open('file.txt','a') as file:
    file.write(new_text)