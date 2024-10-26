class animal:
    def walk(self):
        print("walking...")


class dog(animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof!")
roger = dog("roger", 8)

print(roger.name)
print(roger.age)

roger.bark()
roger.walk()




