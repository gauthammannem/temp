lambda num : num * 2 

multiply = lambda a , b: a*b

print(multiply(2,4))

numbers = [1, 2, 3]

double = lambda a : a*2

result = map(double, numbers)
print(list(result))

result2 = filter(lambda n : n%2 == 0, numbers)
print(list(result2))