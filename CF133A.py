s=input()
l=["H",'Q','9']
check=False
for i in range(len(s)):
    if s[i] in l:
        check=True
        break
    
if check==True:
    print("YES")
else:
    print("NO")

