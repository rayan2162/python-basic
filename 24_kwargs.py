#Kwargs(keyword arguments) = parameter that will pack all arguments into a dictionary

def hello(**inputs):
    print("Hello",end=" ")
    for key,value in inputs.items():
        print(value,end=" ")

hello(f="Rayanul",m="Kader",l="Chowdhury")