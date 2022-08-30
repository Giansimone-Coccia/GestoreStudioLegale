from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
import pickle
import os

#from GestoreStudioLegale.Viste.LoginCliente import LoginCliente


class VistaHomeParcelle(QWidget):

    parcelleList = []
    clientiList = []

    def __init__(self, parent=None):
        super(VistaHomeParcelle, self).__init__(parent)
        grifLayout = QGridLayout()
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista delle parcelle con le relative informazioni")
        textLabel1.setGeometry(QRect(100, 120, 350, 40))
        textLabel1.setFont(QFont('Arial', 12))
        textLabel2.setText(f"{self.getDatiC()}")
        textLabel2.setGeometry(QRect(100, 120, 350, 40))
        textLabel2.setFont(QFont('Arial', 10))
        grifLayout.addWidget(textLabel1, 0, 1)
        grifLayout.addWidget(textLabel2, 0, 2)
        self.setLayout(grifLayout)
        self.resize(600, 500)
        self.setWindowTitle("Parcelle")
        self.show()

    def loadDateP(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                self.parcelleList = list(pickle.load(f))

    def loadFateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clientiList = list(pickle.load(f))

    def getDatiP(self):
        self.loadDateP()
        for parcella in self.parcelleList:
            from GestoreStudioLegale.Viste.LoginCliente import LoginCliente
            if parcella.identificativo == LoginCliente().lineEditUsername.text():
                return parcella

    def getDatiC(self):
        self.loadFateC()
        for cliente in self.clientiList:
            from GestoreStudioLegale.Viste.LoginCliente import LoginCliente
            if cliente.codiceFiscale == LoginCliente().lineEditUsername.text():
                return cliente
