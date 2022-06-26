dic={}
n=int(input())
for i in range(n):
    s=input()
    if s not in dic:
        print("OK")
        dic[s]=1
    else:
        print(f'{s}{dic[s]}')
        dic[s]+=1
