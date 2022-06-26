t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    var=-1
    count=2
    l.sort()
    c=1
    for j in range(len(l)-1):
        if l[j]==l[j+1]:
            c+=1

        if c > count:
            var = l[j]
            count = c
        if l[j]!=l[j+1]:
            c=1


    print(var)
