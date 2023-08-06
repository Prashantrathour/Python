tuple1 = (11, [22, 33], 44, 55)
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
for i in tuple1:
    if type(i)==list:
        i[0]=222
print(tuple1)       
           