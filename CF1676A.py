t=int(input())
for i in range(t):
    s=input()
    sum1=0
    sum2=0
    for j in range(3):
        sum1+=int(s[j])
    for j in range(3,len(s)):
        sum2+=int(s[j])
    if sum1==sum2:
        print("YES")
    else:
        print("NO")