class List:
    def __init__(self,l=None):
        if l is None:
            self.lst=[]
        else:
            self.lst=l
    def __str__(self):
        return f'{self.lst}'
    def append(self,x):
        self.lst+=[x]
    def pop(self,index=None):
        n=len(self.lst)
        if index is None:
            self.lst = self.lst[:n - 1]
            return True
        for i in range(n):
            if i > index:
                self.lst[i - 1] = self.lst[i]
        self.lst = self.lst[:n - 1]

    def remove(self,element):
        n = len(self.lst)
        check = False
        for i in range(n):
            if self.lst[i] == element:
                check = True
                continue
            if check == True:
                self.lst[i - 1] = self.lst[i]
        self.lst = self.lst[:n - 1]
    def insert(self,index,value):
        self.lst.append(0)
        n = len(self.lst) - 1
        for i in range(n - 1, index - 1, -1):
            self.lst[i + 1] = self.lst[i]
        self.lst[index] = value
    def extend(self,extra_list):
        self.lst+=extra_list
    def reverse(self):
        n=len(self.lst)
        for i in range(n//2):
            self.lst[i],self.lst[n-i-1]=self.lst[n-i-1],self.lst[i]
    def sort(self,reverse=False):
        n = len(self.lst)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.lst[j]>self.lst[j+1]:
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]
        if reverse:
            l.reverse()




l=List()
l.append(5)
l.append(6)
l.append(7)
l.append(8)
l.append(10)
l.append(11)
l.append(12)
print(l)
l.remove(7)
print(l)
l.pop(1)
print(l)
l.insert(1,23)
print(l)
l.extend([1,2,35,44])
print(l)
# l.reverse()
# print(l)
l.sort(reverse=True)
print(l)