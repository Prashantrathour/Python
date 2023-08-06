number=[64, 34, 25, 12, 22, 11, 90]

for i in range(0,len(number)-1):
    for j in range(len(number)-1-i):
        if number[j]>number[j+1]:
            number[j],number[j+1]=number[j+1],number[j]
print(number)    