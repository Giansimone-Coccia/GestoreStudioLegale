import os.path

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from GestoreStudioLegale.Servizi.Cliente import Cliente


class LoginCliente(QWidget):

    def __init__(self, parent=None):
        super(LoginCliente, self).__init__(parent)
        self.setWindowTitle('Accesso Cliente')
        self.resize(500, 120)

        layout = QGridLayout()

        self.labelName = QLabel('<font size="4"> Username </font>')
        self.lineEditUsername = QLineEdit()
        self.lineEditUsername.setPlaceholderText('Inserisci codice fiscale')
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
        self.buttonLogin.clicked.connect(self.convalidaPassw())

        self.setLayout(layout)

    def convalidaPassw(self):
        try:
            print("ecco")
            clienti = []
            cliente = Cliente()
            cc = self.lineEditUsername
            cliente.codiceFiscale = cc
            print("Dopo")
            if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
                print("presto")
                with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                    clienti = list(f.read())
                    print("eccoci di nuovo")
                    for cliente in clienti:
                        if cliente.codiceFiscale == cc:
                            print("Accesso eseguito")
                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle('ERRORE')
                            msg.setText('Attenzione, Errore nella lettura del file, riprovare')
                            msg.exec()
                            return
            '''print("Ciao")
            cc = str(self.lineEditUsername)
            cliente = Cliente.ricercaUtilizzatoreCC(cc)
            if cliente:
                if str(self.lineEditPassword) == cliente.password:
                    print("Accesso eseguito")'''
        except:
            msg = QMessageBox()
            msg.setWindowTitle('ERRORE')
            msg.setText('Errore nella lettura del file, riprovare')
            msg.exec()
            return