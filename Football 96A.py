s=input()
oneCount=0
zeroCount=0
#0111111101
for i in range(len(s)):
    if s[i]=='1':
        zeroCount=0
        oneCount+=1
    elif s[i]=='0':
        oneCount=0
        zeroCount+=1
    if oneCount==7 or zeroCount==7:
        break
if oneCount==7 or zeroCount==7:
    print("YES")
else:
    print("NO")