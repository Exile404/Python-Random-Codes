def bigger(s):
    s1=''
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            s1+=(chr(ord(s[i])-32))
        else:
            s1+=s[i]
    return s1
def smaller(s):
    s1 = ''
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            s1 += (chr(ord(s[i]) + 32))
        else:
            s1 += s[i]
    return s1
s=input()
small = 0
cap = 0
for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        cap += 1
    elif 'a' <= s[i] <= 'z':
        small += 1
if cap>small:
    print(bigger(s))
else:
    print(smaller(s))