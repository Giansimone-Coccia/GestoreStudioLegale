from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaHomeUdienze(QWidget):

    udienzeList = []
    clientiList = []

    def __init__(self, parent=None):
        super(VistaHomeUdienze, self).__init__(parent)
        tool = Tools()
        grifLayout = QGridLayout()
        grifLayout.addWidget(tool.rewindButton(self.rewind1), 0, 0)
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista delle udienze con le informazioni relative al cliente")
        textLabel1.setGeometry(QRect(0, 0, 200, 150))
        textLabel1.setFont(QFont('Arial', 10))
        textLabel2.setText(
            'Cliente: ' + '\n' + 'NOME: ' + f"{self.getDatiC()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.getDatiC()['Cognome']}" + '\n' + 'ID: ' + f"{self.getDatiC()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.getDatiC()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.getDatiC()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.getDatiC()['Numero telefono']}")
        textLabel2.setGeometry(QRect(0, 0, 350, 10))
        textLabel2.setFont(QFont('Arial', 10))
        textLabel2.setStyleSheet("border: 1px solid black;")
        textLabel3 = QLabel()
        textLabel3.setText(
            'Udienza: ' + '\n' + 'INTESTATARIO: ' + f"{self.getDatiU()['intestatario']}" + '\n' + 'IMPORTO: ' + f"{self.getDatiU()['importo']}" + '€' + '\n' + 'ID: ' + f"{self.getDatiU()['ID']}" + '\n' + 'IDENTIFICATIVO: ' + f"{self.getDatiU()['identificativo']}")
        textLabel3.setGeometry(QRect(0, 0, 350, 20))
        textLabel3.setFont(QFont('Arial', 10))
        textLabel3.setStyleSheet("border: 1px solid black;")
        grifLayout.addWidget(textLabel2, 1, 1)
        grifLayout.addWidget(textLabel1, 2, 1)
        print("ciao3")
        grifLayout.addWidget(textLabel3, 3, 1)
        self.setLayout(grifLayout)
        self.resize(500, 400)
        self.setWindowTitle("Udienze")
        self.show()

    def loadDateU(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Udienze.pickle'):
            with open('GestoreStudioLegale/Dati/Udienze.pickle', 'rb') as f:
                self.udienzeList = list(pickle.load(f))

    def loadDateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                self.clientiList = list(pickle.load(f))

    def getDatiU(self):
        self.loadDateU()
        tool = Tools()
        for udienza in self.udienzeList:
            if udienza.Cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                return udienza.getDatiUdienza()

    def getDatiC(self):
        self.loadDateC()
        tool = Tools()
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                if cliente.codiceFiscale == str(tool.leggi(n=0)).rsplit()[0]:
                    return cliente.getDatiCliente()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome1 = VistaHomeCliente()
        self.vistaHome1.show()
        self.close()