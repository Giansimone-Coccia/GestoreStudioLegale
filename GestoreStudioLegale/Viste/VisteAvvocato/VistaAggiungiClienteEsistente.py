from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from PyQt5 import QtCore as qtc

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiungiClienteEsistente(QWidget):

    def __init__(self,parent = None):
        super(VistaAggiungiClienteEsistente, self).__init__(parent)

        tool = Tools()
        self.setWindowTitle('Ricerca cliente da aggiungere')
        self.resize(500, 120)
        layout = QGridLayout()
        layout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Inserisci l'id del cliente da aggiungere:")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 10))
        layout.addWidget(textLabel, 1, 0,1,3)
        self.labelIdC = QLabel('<font size="4"> Id cliente </font>')
        self.lineEditIdC = QLineEdit()
        self.lineEditIdC.setPlaceholderText("Inserisci l'id dell'cliente da aggiungere")
        layout.addWidget(self.labelIdC, 2, 0)
        layout.addWidget(self.lineEditIdC, 2, 1)
        self.buttonLogin = QPushButton('Conferma')
        layout.addWidget(self.buttonLogin, 3, 0, 1, 3)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(self.ricercaCliente)
        self.setLayout(layout)

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiungiCliente import VistaAggiungiCliente
        self.vistaH = VistaAggiungiCliente()
        self.vistaH.show()
        self.close()