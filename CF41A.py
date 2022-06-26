def CF41A(s1,s2):
    n=len(s1)
    for i in range(len(s1)):
        if s1[i]!=s2[n-i-1]:
            return False
    return True

s1=input()
s2=input()
check=CF41A(s1,s2)
if check:
    print("YES")
else:
    print("NO")