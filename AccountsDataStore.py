#Draven McConathy
#Stores account data 

class AccountsDataStore:
    def __init__(self):

        #Holds account objects
        self.accountsArray = []

        #Keeps track of the current numberOfAccounts
        self.numberOfAccounts = 0

    #Method to add an account to the data store
    def add_account(self, newAccount):
        #adds new account to accountsArray
        self.accountsArray.append(newAccount)

        #Increases the current number of accounts by 1
        self.numberOfAccounts += 1

    #Method to retrieve account data from the data store
    def get_account_info(self, inputAccountNumber):
        
        #Iterator for while loop that is used to reference index numbers
        index = 0

        #While the index is not equal to the numberOfAccounts
        while index != self.numberOfAccounts:

            #If the inputAccountNumber is equal to the accountNumber at index
            if inputAccountNumber == self.accountsArray[index].accountNumber:
                return self.accountsArray[index]
            else:
                index += 1
                



