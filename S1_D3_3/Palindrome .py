str="mada"
ans=""
for i in range(len(str)-1, -1, -1):
               ans+=str[i]
if str == ans:
        print("the word "+ ans + " is palindrome string")
else : 
        print("the word "+ ans + " is not palindrome string")       