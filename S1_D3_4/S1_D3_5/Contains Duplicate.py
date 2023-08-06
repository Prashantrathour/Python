input_number = [1, 2, 3]

dic = {}

for num in input_number:
    dic[num] = dic.get(num, 0) + 1

print(len(dic.keys())==len(input_number))
