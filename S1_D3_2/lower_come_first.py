str1 = "PyNaTiversity"
low=""
up=""
for i in range(len(str1)):
    if str1[i].isupper():
        up+=str1[i]
    else:
        low+=str1[i]    

print(low+up)