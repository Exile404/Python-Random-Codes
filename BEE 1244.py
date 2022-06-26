def sort(arr,n):
    for i in range(n):
        for j in range(n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


t=int(input())
for i in range(t):
    s=input().split()
    l=sort(s,len(s))
    for j in range(len(l)-1):
        print(l[j],end=" ")
    print(l[len(l)-1])