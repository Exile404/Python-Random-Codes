# s=input().split("WUB")
# print(s)
s=input()
check=True
i=0
n=len(s)
s1=''
while i<n:
    if s[i]=='W' and s[i+1]=='U' and s[i+2]=='B':
        i+=2
        if check==False:
            s1+=" "
            check=True
    else:
        s1+=s[i]
        check=False
    i+=1
print(s1)

