from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys

class AccountCreatorWindow(QMainWindow):
    def __init__(self):
        super(AccountCreatorWindow, self).__init__()

        #Loads the ui created in QTDesigner
        loadUi("AccountCreator.ui", self)

        #connects submitButton to
        #self.submitButton.triggered.connect(self.)
