s1=input()
s2=input()
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        print('1',end="")
    else:
        print('0',end="")
