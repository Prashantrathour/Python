sum=0
count=0
list_data= [10, 20, 30, 40]
for i in range(len(list_data)):
    sum+=list_data[i]
    count=count+1
print("Sum: "+str(sum),"Average: "+str(sum/count))    