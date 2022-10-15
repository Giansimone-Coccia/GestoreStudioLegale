
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin


class LoginAdmin(QWidget):

    def __init__(self, parent=None):
        super(LoginAdmin, self).__init__(parent)

        tool=Tools()
        self.gestore = GestoreSistema()
        self.setWindowTitle('Accesso Admin')
        self.resize(500, 120)
        layout = QGridLayout()
        self.labelName = QLabel('<font size="4"> Username </font>')
        self.lineEditUsername = QLineEdit()
        self.lineEditUsername.setPlaceholderText('Inserisci username')
        layout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        layout.addWidget(self.labelName, 1, 0)
        layout.addWidget(self.lineEditUsername, 1, 1)
        self.labelPassword = QLabel('<font size="4"> Password </font>')
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setPlaceholderText('Inserisci password')
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.labelPassword, 2, 0)
        layout.addWidget(self.lineEditPassword, 2, 1)
        self.buttonLogin = QPushButton('Accedi')
        layout.addWidget(self.buttonLogin, 3, 0, 1, 2)
        layout.setRowMinimumHeight(3, 75)
        self.buttonLogin.clicked.connect(lambda: self.convalidaPassw())
        self.setLayout(layout)

    def convalidaPassw(self):
        user = self.lineEditUsername.text()
        pswrd = self.lineEditPassword.text()
        if self.gestore.loginAdmin(pswrd,user):
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

    def rewind(self):
        from GestoreStudioLegale.Viste.VistaHome import VistaHome
        self.vistaHome = VistaHome()
        self.vistaHome.show()
        self.close()