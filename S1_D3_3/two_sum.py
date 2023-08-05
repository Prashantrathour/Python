Input= [2, 7, 11, 15]
target = 9
i=0
for i in range(len(Input)):
    for j in range(len(Input)):
        if Input[i]+Input[j]==target :
            print(i,j)
        break
         
   