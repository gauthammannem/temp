dogs =["roger",1,"syd",True]

dogs[2]="yyy"
print("gau" in dogs)
print(dogs[0])
print(dogs)
print(dogs[-1])
print(dogs[0:2])
dogs.append("judha")
print(dogs)
dogs.extend(['don', 22]) ## or dogs += ['don', 22]
print(dogs)
dogs.remove("judha")
print(dogs)

dogs.insert(2,"rrr")
print(dogs)
