t=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):

    check=False
    for j in range(len(l)):
        if l[j]==i+1:
            check=True
            l[j]=-1
        if l[j]!=-1 and check==True:
            c+=1
print(c)