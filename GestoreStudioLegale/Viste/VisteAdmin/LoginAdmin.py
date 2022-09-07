import os.path
import pickle

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
#from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin


class LoginAdmin(QWidget):

    def __init__(self, parent=None):
        super(LoginAdmin, self).__init__(parent)
        self.gestore = GestoreSistema()
        self.setWindowTitle('Accesso Admin')
        self.resize(500, 120)
        layout = QGridLayout()
        self.labelName = QLabel('<font size="4"> Username </font>')
        self.lineEditUsername = QLineEdit()
        self.lineEditUsername.setPlaceholderText('Inserisci username')
        layout.addWidget(self.labelName, 0, 0)
        layout.addWidget(self.lineEditUsername, 0, 1)
        self.labelPassword = QLabel('<font size="4"> Password </font>')
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setPlaceholderText('Inserisci password')
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.labelPassword, 1, 0)
        layout.addWidget(self.lineEditPassword, 1, 1)
        self.buttonLogin = QPushButton('Accedi')
        layout.addWidget(self.buttonLogin, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(lambda: self.convalidaPassw())
        self.setLayout(layout)

    def convalidaPassw(self):
            user = self.lineEditUsername.text()
            pswrd = self.lineEditPassword.text()
            print("22222")
            if self.gestore.loginAdmin(pswrd,user):
                print("Accesso eseguito")
                self.show_new()
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('ERRORE')
                msg.setText('Credenziali errate')
                msg.exec()
                return


    def show_new(self):
        self.vistaAdminH = VistaHomeAdmin()
        self.vistaAdminH.show()