s=input()
s1=''
rep='peramoy'
n=len(rep)
x=n
i=0
while i<len(s):
    if s[i:x]==rep:
        s1+='good'
        i+=n
        x+=n
    else:
        s1+=s[i]
        i+=1
        x+=1
print(s1)

