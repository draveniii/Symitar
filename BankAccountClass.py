#Draven McConathy   
#05/30/2024
#Bank account class that keeps and manages account holder information and account funds

class BankAccount:
    def __init__(self, newAccountNumber, name, initialDeposit):
        
        self.accountNumber = newAccountNumber
        self.accountHolderName = name
        self.savings = initialDeposit  
                 



