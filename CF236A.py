s=input()
s1=""
for i in s:
    if i not in s1:
        s1+=i

if len(s1)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")