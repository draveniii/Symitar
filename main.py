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

        #Connects the quick action Create_Account to the open_account_creation_window function
        self.actionCreate_Account.triggered.connect(self.open_account_creation_window)

        self.findAccountButton.clicked.connect(self.open_account)
    
    #Opens a new window to gather information for creating a new account
    def open_account_creation_window(self):
        
        #Initializes the new window and passes the accountDataStore add the created accout to the accountDataStore
        self.window = AccountCreatorWindow(self.accountDataStore)

        #Shows window
        self.window.show()

    #
    #def open_account(self):
    #    pass
    


if __name__ == '__main__':
    #Creates and shows main window
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()
