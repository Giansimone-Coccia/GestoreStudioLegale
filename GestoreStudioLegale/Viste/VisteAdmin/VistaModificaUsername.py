from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaModificaUsername(QWidget):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaModificaUsername, self).__init__(parent)

        self.setWindowTitle('Modifica Username')
        self.resize(500, 120)
        layout = QGridLayout()
        layout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        self.labelOldUser = QLabel('<font size="4"> Vecchio username </font>')
        self.lineEditOldUser = QLineEdit()
        self.lineEditOldUser.setPlaceholderText('Inserisci il vecchio username')
        layout.addWidget(self.labelOldUser, 1, 0)
        layout.addWidget(self.lineEditOldUser, 1, 1)
        self.labelNewUser = QLabel('<font size="4"> Nuovo username </font>')
        self.lineEditNewUser = QLineEdit()
        self.lineEditNewUser.setPlaceholderText('Inserisci nuovo username')
        self.lineEditNewUser.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.labelNewUser, 2, 0)
        layout.addWidget(self.lineEditNewUser, 2, 1)
        self.buttonLogin = QPushButton('Conferma')
        layout.addWidget(self.buttonLogin, 3, 0, 1, 3)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(lambda: self.modificaUser())
        self.setLayout(layout)

    def modificaUser(self):
        tool =Tools()
        passEuser = tool.leggi('CredenzialiAdmin', 0).splitlines()

        if self.lineEditNewUser.text() == self.lineEditOldUser.text():
            msg = QMessageBox()
            msg.setWindowTitle('ERRORE')
            msg.setText('La nuova password coincide con la vecchia password')
            msg.exec()
            return

        if passEuser[1] == self.lineEditOldUser.text():
            tool.salva(f'{passEuser[0]}\n{self.lineEditNewUser.text()}','CredenzialiAdmin')
            msg = QMessageBox()
            msg.setWindowTitle('Username modificato')
            msg.setText('Username modificato con successo')
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