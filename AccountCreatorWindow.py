from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
from BankAccount import BankAccount

class AccountCreatorWindow(QMainWindow):

    def __init__(self, accountDataStore):
        super(AccountCreatorWindow, self).__init__()

        #Loads the ui created for the AccountCreator window in QTDesigner
        loadUi("AccountCreator.ui", self)

        #A reference to the accountDataStore in main
        self.accountDataStore = accountDataStore

        #connects submitButton to the get_input_member_info function
        self.submitButton.clicked.connect(self.get_input_member_info)

    #Method to get the input from the memberName
    def get_input_member_info(self):

        #Getting text from line edit 
        memberName = self.memberNameLineEdit.text()
        memberEmail = self.memberEmailLineEdit.text()
        memberDOB = self.memberDOBLineEdit.text()

        #The share ID number for a savings account
        savings = 0

        #Creates a new BankAccount object
        newAccount = BankAccount(memberName, memberEmail, memberDOB, savings)

        #Adds the new account to the accountDataStore
        self.accountDataStore.add_account(newAccount)

        #Closes Window
        self.close()

        
        

