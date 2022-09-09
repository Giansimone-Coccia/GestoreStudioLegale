from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QScrollArea, QMainWindow
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaHomeUdienze(QMainWindow):

    udienzeList = []
    clientiList = []

    def __init__(self, parent=None):
        super(VistaHomeUdienze, self).__init__(parent)
        tool = Tools()
        self.scroll = QScrollArea()
        self.widget = QWidget()
        grifLayout = QGridLayout()
        grifLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
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
        print("ciao879")
        textLabel3.setText('Udienza: ' + '\n' + 'CITTA TRIBUNALE: ' + f"{self.getDatiU()['Città Tribunale']}" + '\n' + 'TIPO TRIBUNALE: ' + f"{self.getDatiU()['Tipo Tribunale']}" + '\n' + 'ID: ' + f"{self.getDatiU()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{self.getDatiU()['Data e Ora Inizio']}" + '\n' + 'DATA ORA FINE: ' + f"{self.getDatiU()['Data e Ora Fine']}")
        textLabel3.setGeometry(QRect(0, 0, 350, 20))
        textLabel3.setFont(QFont('Arial', 10))
        textLabel3.setStyleSheet("border: 1px solid black;")
        grifLayout.addWidget(textLabel2, 1, 1)
        grifLayout.addWidget(textLabel1, 2, 1)
        print("ciao3")
        grifLayout.addWidget(textLabel3, 3, 1)
        #self.setLayout(grifLayout)
        self.widget.setLayout(grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Udienze')
        self.resize(800, 600)
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
            if cliente.codiceFiscale == str(tool.leggi(n=0)).rsplit()[0]:
                return cliente.getDatiCliente()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome1 = VistaHomeCliente()
        self.vistaHome1.show()
        self.close()