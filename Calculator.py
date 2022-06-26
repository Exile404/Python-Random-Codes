def calculate(l1,l2):
    res=0
    res+=l1[0]
    for i in range(len(l1)-1):
        if l2[i]=="+":
            res+=l1[i+1]
        elif l2[i]=="-":
            res-=l1[i+1]
        elif l2[i]=="*":
            res*=l1[i+1]
        elif l2[i]=="/":
            res/=l1[i+1]
    return res


s=input()
l=['+','-','*','/']
n=len(s)
i=0
res=0
check=True
l1=[]
l2=[]
while i<n:
    x=''
    while True:
        if s[i] in l or i==n-1:
            break
        x+=s[i]
        i+=1
    num=int(x)

    l1.append(num)
    l2.append(s[i])
    i+=1
t=int(str(l1.pop())+l2.pop())
l1.append(t)

sum=calculate(l1,l2)
print(sum)