username='s'
password='s'

pin=1234
balance=100000
class bank:
    def __init__(self):
        self.balance=0
    def bal(self):
        x=int(input("enter your pin:"))
        if pin==x:
            print(self.balance)
        else:
            print("incorrect pin")
    def withdraw(self):
        b=int(input("enter amount:"))
        c=int(input("enter your pin:"))
        if pin==c:
            if b<=self.balanceL:
                self.balance=self.balance-b
                print("Amount withdrawed",b)
                print(self.balance)
            else:
                print("amount greater than balance")
        else:
            print("incorrect pin")
    def deposit(self):
        d=int(input("enter amount:"))
        e=int(input("enter your pin:"))
        if pin==e:
            self.balance=self.balance+d
            print("amount deposited",d)
            print("Your balance is :",self.balance)
        else:
            print("incorrect pin")
        
user1=bank()
while(True):           
    a=int(input('''
                1.login
                2.exit
                enter your choice:'''))
    
    if a==1:
        f=input("enter username:")
        g=input("enter password:")
        if username==f and password==g:
            while(True):
        
                us=int(input('''
                            1.Check balance
                            2.Withdraw
                            3.Deposit
                            4.go back
                            enter your choice:'''))
                if us==1:
                    user1.bal()
                
                elif us==2:
                    user1.withdraw()
                elif us==3:
                    user1.deposit()
                elif us==4:
                    break
                else:
                    print("invalid choice")
                
        else:
            print("incorrect username or password")
    elif a==2:
        break
           
           
            
