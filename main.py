#Draven McConathy
#05/29/2024
#Imitation of Symitar, a core prossesing system for financial institutions

from BankAccountClass import *

def main():

    print("Welcome to Symitar\n\n")
    
    #array that stores created accounts
    accountsArray = []

    userInput = None

    #Shows menu and gets user input
    while userInput != 3:
        print_menu()
        userInput = get_menuInput()
        if userInput == 1:
            pass
        elif userInput == 2:
            create_account(accountsArray)
        else:
            print("Goodbye!")

def print_menu():
    print("1. Find an account\n")
    print("2. Create an Account\n")
    print("3. Quit\n")

#Gets account number from user and returns that number
def get_account_number():
    inputAccountNumber = int(input("Please enter an account number: "))
    return inputAccountNumber

#Gets an input from user for menu selection and validates said input
def get_menuInput():
    userInput = int(input())

    #Makes sure userInput is valid and continues to get input if it is not
    while userInput < 1 or userInput > 3:
        userInput = int(input("Please enter one of the menu options 1-3: "))
    
    return userInput

#Generates an account number, collects information needed to create account, and creates a BankAccount object which is stored in the "accounts" array
def create_account(accountsArray):
   #Creates the new account
   newAccount = BankAccount()

   #Creates a member object and adds the member to the account
   newAccount.add_member()

   #Creates a share and adds the share to the account
   newAccount.add_share()

   #adds created account to the accountsArray
   accountsArray.append(newAccount)



if __name__ == "__main__":
    main()



