list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
ans=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        ans.append(list1[i]+list2[j])
print(ans)