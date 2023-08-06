def climbing(n):
    if ( n<0):
        return 0
    if ( n==0):
        return 1
    return climbing(n-1)+climbing(n-2)  

print(climbing(5))