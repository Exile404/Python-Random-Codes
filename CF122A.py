n=input()
n1=int(n)
if n1%4==0 or n1%7==0 or n1%47==0 or n1%74==0:
    print("YES")
else:
    check=True
    for i in n:
        if i!='4' and i!='7':
            check=False
            break
    if check:
        print("YES")
    else:
        print("NO")