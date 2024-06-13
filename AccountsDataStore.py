#Draven McConathy
#Stores account data 

class AccountsDataStore:
    def __init__(self):

        #Holds account objects
        self.accountsArray = []

    #Method to add an account to the data store
    def add_account(self, newAccount):
        self.accountsArray.append(newAccount)

    #Method to retrieve account data from the data store
    def get_account_info(self, inputAccountNumber):
        
        #Iterator for while loop that is used to reference index numbers
        index = 0

        #While the inputAccountNumber does not equal the accountNumber at index position in array, keep searching
        while inputAccountNumber != self.accountsArray[index].accountNumber:

            #If the inputAccountNumber is equal to the accountNumber at index
            if inputAccountNumber == self.accountsArray[index].accountNumber:
                return self.accountsArray[index]
            else:
                pass



