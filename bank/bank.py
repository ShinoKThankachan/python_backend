class bank:
    def balance():
        x=int(input("enter your pin:"))
        print("Your bank balance is $$$$$")
    def withdraw():
        b=int(input("enter amount:"))
        c=int(input("enter your pin:"))
        print("Amount withdrawed",b)
    def deposit():
        d=int(input("enter amount:"))
        e=int(input("enter your pin:"))
        print("amount deposited",d)
user1=bank
while(True):           
    a=int(input('''
                1.login
                2.exit
                enter your choice:'''))
    
    if a==1:
        f=input("enter username:")
        g=input("enter password:")
        
        us=int(input('''
                     1.Check balance
                     2.Withdraw
                     3.Deposit
                     enter your choice:'''))
        if us==1:
           user1.balance()
           
        elif us==2:
            user1.withdraw()
        elif us==3:
            user1.deposit()
        else:
            print("invalid choice")
    elif a==2:
        break
           
           
            
