l=list(map(int,input().split()))
l.sort()
for i in range(len(l)-1):
    print(l[3]-l[i],end=" ")
