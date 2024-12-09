class Bank:
    def __init__(self, a, n, t , b):
        self.ac = a
        self.name = n
        self.type = t
        self.bal = b
        
    def deposit(self, a1):
        self.bal += a1
        print("Account Balance:",self.bal)
    
    def withdraw(self, a2):
        if self.bal<a2:
            print("invalid")
        
        else:
            self.bal -=a2
            print("Withdrawal Balance:",self.bal)
            
    def display(self):
        print("****ACCOUNT DETAILS****")
        print("Acc no:",self.ac)
        print("Name:",self.name)
        print("Acc Type:",self.type)
        print("Acc Balance",self.bal)

print("****ENTER ACCOUNT DETAILS****")
a=int(input("Enter the Acc no:"))
n=input("Enter Name:")
t=input("Enter Account Type:")
b=int(input("Enter Balance:"))


obj1= Bank(a, n, t, b)
obj1.display()
a1=int(input("Enter the Amount to Deposit:"))
obj1.deposit(a1)

obj2= Bank(a, n, t, b)
a2=int(input("Enter the Amount to Withdraw:"))
obj2.withdraw(a2)
