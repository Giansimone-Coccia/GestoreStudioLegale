from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema

from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato

from GestoreStudioLegale.Utilities.Utilities import Tools


class LoginAvvocato(QWidget):

    def __init__(self, parent=None):

        super(LoginAvvocato, self).__init__(parent)
        self.setWindowTitle('Accesso Avvocato')
        self.resize(500, 120)
        tool = Tools()
        layout = QGridLayout()
        self.labelName = QLabel('<font size="4"> Username </font>')
        self.lineEditUsername = QLineEdit()
        self.lineEditUsername.setPlaceholderText('Inserisci codice fiscale')
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
        tool = Tools()
        cc = self.lineEditUsername.text()
        pswrd = self.lineEditPassword.text()
        gestore = GestoreSistema()
        tool.salva(str(self.lineEditUsername.text()))

        if gestore.loginAvvocato(pswrd, cc):
            self.show_new()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('ERRORE')
            msg.setText('Credenziali errate')
            msg.exec()
            return


    def show_new(self):
        self.vistaAvvocatoH = VistaHomeAvvocato()
        self.vistaAvvocatoH.show()

    def rewind(self):
        from GestoreStudioLegale.Viste.VistaHome import VistaHome
        self.vistaH = VistaHome()
        self.vistaH.show()
        self.close()
