lists=[64, 25, 12, 22, 11]
for i in range (0,len(lists)):
    min_index=i
    for j in range(i+1,len(lists)):
        if(lists[j]<lists[min_index]):
            min_index =j
    lists[i],lists[min_index]=lists[min_index],lists[i]   

print(lists)         