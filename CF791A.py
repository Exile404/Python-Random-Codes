limak,bob=list(map(int,input().split()))
count=0
while limak<=bob:
    limak*=3
    bob*=2
    count+=1
print(count)
