arr=[40,30,10,20,50]
n=len(arr)
for i in range(n):
    minn=i
    for j in range(i+1,n):
        if arr[j]<arr[minn]:
            minn=j
    arr[i],arr[minn]=arr[minn],arr[i]
    #temp=arr[i]
    #arr[i]=arr[minn]
    #arr[minn]=temp
print(arr)