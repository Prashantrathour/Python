n=5
i=0
fibo_initial=[0,1]
while i<n-2:
    fibo_initial.append(fibo_initial[-1]+fibo_initial[-2])
    i+=1
print(fibo_initial)    