class Bank:
    def __init__(self,name,ID,AccountNO):
        self.name=name
        self.ID=ID
        self.AccountNO=AccountNO
    def details(self):
        print("---------CUSTOMER DETAILS---------")
        print(f"Name : {self.name}\n"
              f"ID : {self.ID}\n"
              f"Account NO : {self.AccountNO}\n")


class Customer(Bank):
    def __init__(self,username,password,name,ID,AccountNO):
        self.username=username
        self.password=password
        super().__init__(name,ID,AccountNO)
    def allDetails(self):
        super().details()
        print(self.username)
        print(self.password)

c1=Customer('Dhr123',"********","Dhrubo",20101427,47556455645)
c1.allDetails()
