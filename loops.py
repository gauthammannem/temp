
condition = True

while condition == True:
     print("hi")
     condition = False


count = 0
while count < 10:
     print("its true")
     count = count + 1

print("after the loop")

items = [1,2,3,4]
for item in items:
     print(item)


for item in range(6):
     print(item)


items = [1,2,3,4]
for index, item in enumerate(items):
     print(index, item)
