def greet():
    print("hi")
    print("good morning")

def add_sub(x,y):
    c= x+y
    d= x-y
    return c,d 

result1,result2 = add_sub(5,4)
greet()
print(result1)
print(result2)

def hello(name , age):
    print('hello'+name + "you are " + str(age) + " years ")

hello(" efc" ,40)
hello(" efhfi" ,32)    
hello(" ndweib" ,221)

def change(value):
    value["name"] = "syd"
val = {"name" : "baue"}
change(val)

print(val)

def new(name):
    print("hello" + name + "!")
    return name, "beau" , 8

print(new("syd"))