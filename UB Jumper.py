def sort(arr,n):
    for i in range(n - 1):
        minn = i
        for j in range(i + 1, n):
            if arr[j] < arr[minn]:
                minn = j
        arr[i], arr[minn] = arr[minn], arr[i]
    return arr
while True:
    l=input()
    if l=="STOP":
        break
    l=list(map(int,l.split()))
    l1=[]
    for i in range(len(l)-1):
        l1.append(abs(l[i]-l[i+1]))
    l1=sort(l1,len(l1))
    check=True
    for i in range(len(l1)):
        if i+1!=l1[i]:
            check=False
            break
    if check==True:
        print("UB Jumper")
    else:
        print("Not UB Jumper")

