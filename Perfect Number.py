def perfect_number(x):
    sum=0
    for i in range(1, x):
        if x % i == 0:
            sum+=i
    if sum==x:
        return True
    else:
        return False

a,b=map(int,input().split())
for i in range(a,b+1):
    if perfect_number(i)==True:
        print(i)