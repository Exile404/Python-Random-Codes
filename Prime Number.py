n=int(input())
check=True
for i in range(2,n):
    if n%i==0:
        check=False
        break
if check==True:
    print("Prime Number")
else:
    print("Not a Prime Number")