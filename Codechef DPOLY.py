t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))#2 5 4 6 7
    l1=[]
    for j in range(len(l)):
        if l[j]!=0:
            l1+=[j]
    print(l1[len(l1)-1])
