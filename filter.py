numbers =[1,2,3,4,5]

def iseven(n):
    return n%2 == 0

result = filter(iseven, numbers)
print(list(result))
