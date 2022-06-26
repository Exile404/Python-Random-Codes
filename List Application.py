def len(l):
    count=0
    for i in l:
        count=count+1
    return count
def append(l,ele):
    l+=[ele]
    return l
def extend(l,extra_list):
    l+=extra_list
    return l
def pop(l,index=None):
    if index==None:
        l=l[:len(l)-1]
        return l
    for i in range(len(l)):
        if i>index:
            l[i-1]=l[i]
    l = l[:len(l) - 1]
    return l
def remove(l,element):
    check=False
    for i in range(len(l)):
        if l[i]==element:
            check=True
            continue
        if check==True:
            l[i - 1] = l[i]
    l = l[:len(l) - 1]
    return l
def insert(l,index,value):
    l=append(l,0)
    n=len(l)-1
    for i in range(n-1,index-1,-1):
        l[i+1]=l[i]
    l[index]=value
    return l

l=[2,1,3,74,6,8,7,6]
sz=len(l)
print(sz)
l=append(l,100)
print(l)
l=extend(l,[5,6,7,8])
print(l)
l=pop(l)
print(l)
l=pop(l,3)
print(l)
l=remove(l,100)
print(l)
l=insert(l,3,100)
print(l)
