# n=int(input())
# m=int(input())
# a=int(input())
n,m,a=list(map(int,input().split()))
ans=0
if n%a!=0 and m%a!=0:
    ans=((n//a)+1)*((m//a)+1)
elif n%a!=0 and m%a==0:
    ans=((n//a)+1)*((m//a))
elif n%a==0 and m%a!=0:
    ans = (n // a)  * ((m // a)+1)
else:
    ans = (n // a) * (m // a)

print(ans)

