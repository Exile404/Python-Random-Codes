n,t=list(map(int,input().split()))
s=input()
l=[]
for i in s:
    l.append(i)
i=0
while i<t:
    j=0
    while j<n-1:
        if l[j]=='B' and l[j+1]=='G':
            l[j],l[j+1]=l[j+1],l[j]
            j+=1
        j+=1
    i+=1
for i in l:
    print(i,end="")