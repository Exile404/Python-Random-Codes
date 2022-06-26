class Bank:
    def __init__(self,name,NID,Address,Phone):
        self.__name=name
        self.__NID=NID
        self.__Address=Address
        self.__Phone=Phone
        self.__balance=1000
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setNID(self,x):
        self.__NID=x
    def getNID(self):
        return self.__NID
    def setAddress(self,Addr):
        self.__Address=Addr
    def getAddress(self):
        return self.__Address
    def getBalance(self):
        return self.__balance
    def setBalance(self,x):
        self.__balance=x
    def addmoney(self,x):
        self.__balance+=x
    def transaction(self,x):
        a=self.getBalance()
        if a<1000:
            print("Not Enough Money")
        else:
            print("Transaction Successful")
            a-=x
            self.setBalance(a)
            print("Current Money:",self.getBalance())
    def balanceCheck(self):
        print(self.getBalance())
    def details(self):
        print(f"Name : {self.getname()}\n"
              f"NID : {self.getNID()}\n"
              f"Address : {self.getAddress()}\n"
              f"Phone : {self.__Phone}\n"
              f"Balance: {self.getBalance()}")

b=Bank('Dhrubo',21001212121,'Mirpur',173974556)
# b.setname('TH')
# print(b.getname())
b.details()
