import math

a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    x=math.sqrt(i)
    y=int(x)
    if x==y:
        c+=1
print(c)