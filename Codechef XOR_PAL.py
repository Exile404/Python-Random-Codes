t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    x=len(s)
    c=0
    for j in range((x//2)):
        if s[j]!=s[x-j-1]:
            c+=1
    print(c)