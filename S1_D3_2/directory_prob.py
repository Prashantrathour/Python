employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dic={}
for i in range(len(employees)):
    dic[employees[i]]=defaults
print(dic)    