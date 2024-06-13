from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
from AccountCreatorWindow import AccountCreatorWindow
from AccountsDataStore import AccountsDataStore

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        #Loads the ui for the main page made in QTDesigner
        loadUi("Symitar.ui", self)

        #Initializes instance of AccountsDataStore
        self.accountDataStore = AccountsDataStore()

        #Contains a reference of the currentWorkingAccount 
        self.currentWorkingAccount = None

        #Connects quick actions to methods
        self.actionCreate_Account.triggered.connect(self.open_account_creation_window)

        #Connects buttons to methods
        self.findAccountButton.clicked.connect(self.change_current_working_account)
    
    #Opens a new window to gather information for creating a new account
    def open_account_creation_window(self):
        
        #Initializes the new window and passes the accountDataStore to the created account to the accountDataStore
        self.window = AccountCreatorWindow(self.accountDataStore)

        #Shows window
        self.window.show()

    #Takes the account number from the line edit and uses it to find the matching account, if the account is found a referenced is passed to the main window
    def change_current_working_account(self):

        #Getting account number from line edit
        currentWorkingAccountNumber = int(self.findAccountField.text())

        #Gives a reference of an account from the accountDataStore
        self.currentWorkingAccount = self.accountDataStore.get_account_info(currentWorkingAccountNumber)

        #Updates all account information to the ui
        self.nameLabel.setText(self.currentWorkingAccount.members[0].get_memberName())
        self.accountNumberLabel.setText(str(self.currentWorkingAccount.get_accountNumber()))
        self.memberNameLabel.setText(self.currentWorkingAccount.members[0].get_memberName())
        self.DOBLabel.setText(self.currentWorkingAccount.members[0].get_memberDOB())
        self.shareLabel0.setText(self.currentWorkingAccount.shares[0].get_shareName())
        self.balanceLabel0.setText(str(self.currentWorkingAccount.shares[0].get_currentBalance()))


    


if __name__ == '__main__':
    #Creates and shows main window
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()
