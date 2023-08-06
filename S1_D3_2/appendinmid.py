s1 = "Ault"
s2 = "Kelly"
mid=int(len(s1)/2)
newlist=list(s1)
newlist.insert(mid,s2)
print("".join(newlist))