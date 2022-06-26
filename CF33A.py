s=input().split('+')
s.sort()
print(s)
for i in range(len(s)):
    if i==0:
        print(s[i],end='')
    else:
        print(f'+{s[i]}',end='')
print()
