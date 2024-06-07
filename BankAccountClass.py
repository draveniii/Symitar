#Draven McConathy   
#05/30/2024
#Bank account class that keeps and manages account holder information and account funds

from MemberClass import *
from ShareClass import *

class BankAccount:

    #Keeps track of the account numbers used so far, incrememting with each account created
    nextAccountNumber = 1

    def __init__(self):
        self.accountNumber = self.nextAccountNumber
        self.members = []
        self.shares = []

        self.accountNumber += 1

    def get_accountNumber(self):
        return self.accountNumber

    #Creates a member object using user inputs and adds the member to the member list on the account
    def add_member(self):
        newMemberName = input("Please enter member name: ")
        newMemberEmail = input("Please enter the members email: ")
        newMemberDOB = input("Please enter the members date of birth: ")
        newMember = Member(newMemberName, newMemberEmail, newMemberDOB)
        self.members.append(newMember)

    #Gets user input for the type of share to create, creates the share using given default parameters, and adds the share to the account
    def add_share(self):
        print("1. Savings\n")
        print("2. Checking\n")
        print("3. Cancel\n")
        shareInput = input("What share should be added to the account: ")

        #Creates and adds a share to the account depending on the userInput
        if shareInput == 1:
            savings = Share(0, "Savings", .05, 25)
            self.members.append(savings)
        if shareInput == 2: 
            checking  = Share(1, "Checking", .00, 0)
            self.shares.append(checking)
        else:
            pass
        




    
        

    
        
                 



