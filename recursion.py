def factorian(n):
    if n==1:
        return 1
    return n* factorian(n-1)
print(factorian(91))
