from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox


class VistaModificaPassword(QWidget):

    def __init__(self, parent=None):
        super(VistaModificaPassword, self).__init__(parent)
        self.setWindowTitle('Modifica Password')
        self.resize(500, 120)

        layout = QGridLayout()

        self.labelOldPassword = QLabel('<font size="4"> Vecchia password </font>')
        self.lineEditOldPassw = QLineEdit()
        self.lineEditOldPassw.setPlaceholderText('Inserisci la vecchia password')
        layout.addWidget(self.labelOldPassword, 0, 0)
        layout.addWidget(self.lineEditOldPassw, 0, 1)

        self.labelNewPassword = QLabel('<font size="4"> Nuova Password </font>')
        self.lineEditNewPassword = QLineEdit()
        self.lineEditNewPassword.setPlaceholderText('Inserisci nuova password')
        self.lineEditNewPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.labelNewPassword, 1, 0)
        layout.addWidget(self.lineEditNewPassword, 1, 1)

        self.buttonLogin = QPushButton('Conferma')
        layout.addWidget(self.buttonLogin, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(lambda: self.modificaPassw())

        self.setLayout(layout)

    def modificaPassw(self):
        tool = Tools()
        cc = self.lineEditUsername.text()
        pswrd = self.lineEditPassword.text()
        print("22222")
        gestore = GestoreSistema()
        tool.salva(str(self.lineEditUsername.text()))
        #tool.salvaAppend(str(self.lineEditPassword.text()))

        if gestore.loginCliente(pswrd, cc):
            print("Accesso eseguito")
            self.show_new()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('ERRORE')
            msg.setText('Credenziali errate')
            msg.exec()
            return
