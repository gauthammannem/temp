dog = { "name": "roger" , "age": 8 }

dog['name']="sdd"
print(dog['name'])
print(dog)
print(dog.keys())
print(dog.values())
print(dog.items())
dog['fav food']="meat"
print(dog)
dogcopy = dog.copy
del dog['age']
print(dog)