class Atm(object):
    def __init__(self,BalanceEnquiry,CashWithDrawl,AccountName,CardNumber,Pin,CashDeposit):
        self.BalanceEnquiry = BalanceEnquiry
        self.CashWithDrawl = CashWithDrawl
        self.AccountName = AccountName
        self.CardNumber = CardNumber
        self.Pin = Pin
        self.CashDeposit = CashDeposit
       

    def start(self):
        print("Hello!",self.AccountName)
    

    def Withdrawal(self):
       self.CashWithDrawl=int(input("How much do you want to withdraw?"))
       if self.BalanceEnquiry>self.CashWithDrawl:
           self.BalanceEnquiry= self.BalanceEnquiry-self.CashWithDrawl
           print("Your current BalanceEnquiry is now",self.BalanceEnquiry)
            

       else:
           print("You cannot withdraw more than",self.BalanceEnquiry)

    def Deposit(self):
        self.CashDeposit=int(input("How much do you want to Deposit?"))
        self.BalanceEnquiry=self.CashDeposit+ self.BalanceEnquiry
        print("Your current BalanceEnquiry is now",self.BalanceEnquiry)

    def Receipt(self):
        print("")
        print("")
        print("")
        print("")
        
        print("THIS IS YOUR RECEIPT")
        print("Confirmation Details:-")
        print("This is your account name:-",self.AccountName)
        print("This is your card Number:-",self.CardNumber)
        print("Total Withdrawal:-",self.CashWithDrawl,"Rs")
        print("Total Deposit:-",self.CashDeposit,"Rs")
        print("This is your total bank balance:-",self.BalanceEnquiry,"Rs")
        print("Thank you for your transaction")


    


customer=Atm(7000,100,"Vishnu",1003,1234,10)
customer.start()
customer.Withdrawal()
customer.Deposit()
customer.Receipt()

    
        
  


    