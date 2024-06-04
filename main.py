#Draven McConathy
#05/29/2024
#Imitation of Symitar, a core prossesing system for financial institutions

def main():
    print("Welcome to Symitar\n\n")

    userInput = None

    #Shows menu and gets user input
    while userInput != 3:
        print_menu()
        userInput = get_menuInput()
        if userInput == 1:
            get_account_number

def print_menu():
    print("1. Find an account\n")
    print("2. Create an Account\n")
    print("3. Quit\n")

def get_account_number():
    inputAccountNumber = input("Please enter an account number: ") #Gets account number from user
    return inputAccountNumber

def get_menuInput():
    userInput = input()

    #Makes sure userInput is valid and continues to get input if it is not
    while userInput < 1 or userInput > 3:
        userInput = input("Please enter one of the menu options 1-3: ")
    
    return userInput
        

if __name__ == "__main__":
    main()



