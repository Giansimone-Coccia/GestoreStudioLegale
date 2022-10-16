from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaModificaPassword(QWidget):

    def __init__(self, parent=None):
        super(VistaModificaPassword, self).__init__(parent)
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        tool = Tools()
        self.setWindowTitle('Modifica Password')
        self.resize(500, 120)
        layout = QGridLayout()
        layout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        self.labelOldPassword = QLabel('<font size="4"> Vecchia password </font>')
        self.lineEditOldPassword = QLineEdit()
        self.lineEditOldPassword.setPlaceholderText('Inserisci la vecchia password')
        layout.addWidget(self.labelOldPassword, 1, 0)
        layout.addWidget(self.lineEditOldPassword, 1, 1)
        self.labelNewPassword = QLabel('<font size="4"> Nuova Password </font>')
        self.lineEditNewPassword = QLineEdit()
        self.lineEditNewPassword.setPlaceholderText('Inserisci nuova password')
        self.lineEditNewPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.labelNewPassword, 2, 0)
        layout.addWidget(self.lineEditNewPassword, 2, 1)
        self.buttonLogin = QPushButton('Conferma')
        layout.addWidget(self.buttonLogin, 3, 0, 1, 3)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(lambda: self.modificaPassw())
        self.setLayout(layout)

    def modificaPassw(self):
        tool =Tools()
        passEuser = tool.leggi('CredenzialiAdmin', 0).splitlines()

        if self.lineEditNewPassword.text() == self.lineEditOldPassword.text():
            msg = QMessageBox()
            msg.setWindowTitle('ERRORE')
            msg.setText('La nuova password coincide con la vecchia password')
            msg.exec()
            return

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

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaModificaCredenziali import VistaModificaCredenziali
        self.vistaHome = VistaModificaCredenziali()
        self.vistaHome.show()
        self.close()
