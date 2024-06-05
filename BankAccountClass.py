#Draven McConathy   
#05/30/2024
#Bank account class that keeps and manages account holder information and account funds

class BankAccount:
    def __init__(self, newAccountNumber):
        self.accountNumber = newAccountNumber
        self.members = []
        self.shares = []

    def get_accountNumber(self):
        return self.accountNumber

    def add_member(self, newMember):
        self.members.append(newMember)

    def add_share(self, newShare):
        self.shares.append(newShare)

    
        
                 



