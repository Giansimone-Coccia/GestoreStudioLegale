from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaHomeParcelle(QWidget):

    parcelleList = []
    clientiList = []

    def __init__(self, parent=None):
        super(VistaHomeParcelle, self).__init__(parent)
        grifLayout = QGridLayout()
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista delle parcelle con le relative informazioni relative al cliente")
        textLabel1.setGeometry(QRect(0, 0, 200, 150))
        textLabel1.setFont(QFont('Arial', 10))
        textLabel2.setText('Cliente: '+'\n'+ 'NOME: '+f"{self.getDatiC()['Nome']}"+ '\n'+'COGNOME: '+f"{self.getDatiC()['Cognome']}"+'\n'+'ID: '+f"{self.getDatiC()['Id']}"+'\n'+'CODICE FISCALE: '+f"{self.getDatiC()['Codice fiscale']}"+'\n'+'EMAIL: '+f"{self.getDatiC()['Email']}"+'\n'+'NUMERO TELEFONO: '+f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Times', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        textLabel3 = QLabel()
        textLabel3.setText('Parcella: '+'\n'+ 'INTESTATARIO: '+f"{self.getDatiP()['intestatario']}"+ '\n'+'IMPORTO: '+f"{self.getDatiP()['importo']}"+'€'+'\n'+'ID: '+f"{self.getDatiP()['ID']}"+'\n'+'IDENTIFICATIVO: '+f"{self.getDatiP()['identificativo']}")
        textLabel3.setGeometry(QRect(0, 0, 350, 20))
        textLabel3.setFont(QFont('Times', 10))
        textLabel3.setStyleSheet("border: 1px solid black;")
        grifLayout.addWidget(textLabel2, 0, 0)
        grifLayout.addWidget(textLabel1, 1, 0)
        grifLayout.addWidget(textLabel3, 2, 0)
        self.setLayout(grifLayout)
        self.resize(500, 400)
        self.setWindowTitle("Parcelle")
        self.show()

    def loadDateP(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                self.parcelleList = list(pickle.load(f))

    def loadDateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clientiList = list(pickle.load(f))

    def getDatiP(self):
        self.loadDateP()
        tool = Tools()
        for parcella in self.parcelleList:
            if parcella.Cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                return parcella.getDatiParcellaCliente()

    def getDatiC(self):
        self.loadDateC()
        tool = Tools()
        print(tool.leggi())
        for cliente in self.clientiList:
<<<<<<< HEAD
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
=======
            if cliente.codiceFiscale == str(tool.leggi(n=0)).rsplit()[0]:
>>>>>>> ffd2d69efab453c20531fd393835bd774ee7fb4f
                return cliente.getDatiCliente()