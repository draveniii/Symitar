#Share Class
#Draven McConathy  
#06/04/2024
#Outlines the contents on a share including share name, share ID, interest rate, and minimum balance

class Share:
    def __init__(self, IDNumber, name, rate, minimumBalance):
        self.shareID = IDNumber
        self.shareName = name
        self.interestRate = rate
        self.minimumBalance = minimumBalance
        self.currentBalance = 0
 
    def change_interestRate(self, newInterestRate):
        self.interestRate = newInterestRate

    def withdraw_funds(self, amountToWithdraw):
        #If the account does not have the funds to cover the withdraw, stop the withdraw.
        if amountToWithdraw <= self.currentBalance - self.minimumBalance:
            self.currentBalance -= amountToWithdraw
        else:
            print("Non sufficient funds")

    def deposit_funds(self, amountToDeposit):
        self.currentBalance += amountToDeposit

    def get_currentBalance(self):
        return self.currentBalance
    
    def get_shareName(self):
        return self.shareName

    
    