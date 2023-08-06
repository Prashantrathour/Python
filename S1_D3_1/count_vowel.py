vowel="aeiou"
word="hello worldaaaa"
count=0
for i in range(len(word)):
    if vowel.__contains__(word[i]):
        count+=1
print(count)        