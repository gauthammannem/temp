from functools import reduce

exps =[("dinner", 80),("car", 180)]

sum = reduce(lambda a, b: a[1] + b[1], exps)

print(sum)
