s=input()
s1=''
for i in range(len(s)):
    if 'A'<=s[i]<'Z':
        x=ord(s[i])+32
        y=chr(x)
        s1+=y
    else:
        s1+=s[i]
vowel="AEIOUYaeiouy"
res=''
for i in range(len(s1)):
    if s1[i] not in vowel:
        res+=("."+s1[i])
print(res)

