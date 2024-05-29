#Draven McConathy
#05/29/2024
#Imitation of Symitar, a core prossesing system for financial institutions

def main():
    print("Welcome to Symitar\n")

    currentAccount = get_account_number()
    print(currentAccount)

def get_account_number():
    inputAccountNumber = input("Please enter a four digit account number: ") #Gets account number from user
    return inputAccountNumber

if __name__ == "__main__":
    main()



