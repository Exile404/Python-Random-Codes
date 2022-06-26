dic={1:'AJS',2:'BKT',3:'CLU',4:'DMV',5:'ENW',6:'FOX',7:'GPY',8:'HQZ',9:'IR'}



s=input()
sum=0
s=s.upper()
for j in range(len(s)):
    for k,v in dic.items():
        if s[j] in dic[k]:
            sum+=k
            break
while len(str(sum))!=1:
    sum=str(sum)
    x=0
    for j in range(len(sum)):
        x+=int(sum[j])
    sum=x
print(sum)

