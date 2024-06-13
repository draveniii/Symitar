#Draven McConathy   
#05/30/2024
#Bank account class that keeps and manages account holder information and account funds

from Member import *
from Share import *

class BankAccount:

    #Keeps track of the account numbers used so far, incrememting with each account created
    nextAccountNumber = 1

    def __init__(self, newMemberName, newMemberEmail, newMemberDOB, Savings):
        #Assigns an account number to the new account
        self.accountNumber = self.nextAccountNumber

        #Incrememnts the number of accounts that have been made
        self.nextAccountNumber += 1

        #Declares the member and share arrays
        self.members = []
        self.shares = []

        #adds a member to the account
        self.add_member(newMemberName, newMemberEmail, newMemberDOB)

        #adds a share to the account
        self.add_share(Savings)

    def get_accountNumber(self):
        return self.accountNumber

    #Creates a member object using user inputs and adds the member to the member list on the account
    def add_member(self, newMemberName, newMemberEmail, newMemberDOB):
        newMember = Member(newMemberName, newMemberEmail, newMemberDOB)
        self.members.append(newMember)

    #Gets user input for the type of share to create, creates the share using given default parameters, and adds the share to the account
    def add_share(self, shareInput):

        #Creates and adds a share to the account depending on the userInput
        if shareInput == 0:
            savings = Share(0, "Savings", .05, 25)
            self.members.append(savings)
        elif shareInput == 1: 
            checking  = Share(1, "Checking", .00, 0)
            self.shares.append(checking)
        else:
            pass
        




    
        

    
        
                 



