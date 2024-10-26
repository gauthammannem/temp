done = 0

print(type(done))

if done:
    print("yes")
else:
    print("no")


ingredients_purchased = True
meal_cooked = False


ready_to_serve1 = all([ingredients_purchased,meal_cooked]) 
ready_to_serve2 = any([ingredients_purchased,meal_cooked])     
print(ready_to_serve1)
print(ready_to_serve2)