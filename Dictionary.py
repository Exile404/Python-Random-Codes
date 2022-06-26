# dic={1:'Dhrubo','2':4578,'487':[1,2,3,4,96]}
# print(dic['487'][2])
dic={}
n=int(input())
for i in range(n):
    s=input().split()
    if s[0] not in dic:
        l=[]
        l.append(s[1])
        dic[s[0]]=l
    else:
        dic[s[0]].append(s[1])
print(dic)

dic={2:['A','B','C']}