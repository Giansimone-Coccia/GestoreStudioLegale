from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaModificaPassword(QWidget):

    def __init__(self, parent=None):
        super(VistaModificaPassword, self).__init__(parent)
        self.setWindowTitle('Modifica Password')
        self.resize(500, 120)

        layout = QGridLayout()

        self.labelOldPassword = QLabel('<font size="4"> Vecchia password </font>')
        self.lineEditOldPassword = QLineEdit()
        self.lineEditOldPassword.setPlaceholderText('Inserisci la vecchia password')
        layout.addWidget(self.labelOldPassword, 0, 0)
        layout.addWidget(self.lineEditOldPassword, 0, 1)

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
        tool =Tools()
        passEuser = tool.leggi('CredenzialiAdmin', 0).splitlines()
        print(passEuser)

        if passEuser[0] == self.lineEditOldPassword.text():

            tool.salva(f'{self.lineEditNewPassword.text()}\n{passEuser[1]}','CredenzialiAdmin')

            msg = QMessageBox()
            msg.setWindowTitle('Password modificata')
            msg.setText('Password modificata con successo')
            msg.exec()
            self.close()
            return
        else:
            msg = QMessageBox()
            msg.setWindowTitle('ERRORE')
            msg.setText('Vecchia Password errata')
            msg.exec()
            return
