arr=[40,30,10,20,50]
n=len(arr)
for i in range(1,n):
    ele=arr[i]
    j=i-1
    while j>=0 and ele<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=ele
print(arr)