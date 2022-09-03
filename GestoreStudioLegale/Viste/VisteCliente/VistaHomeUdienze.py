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

        grifLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista delle Udienze con le relative informazioni")
        textLabel1.setGeometry(QRect(100, 120, 350, 40))
        textLabel1.setFont(QFont('Arial', 12))
        textLabel2.setText(f"{self.getDatiC()}")
        textLabel2.setGeometry(QRect(100, 120, 350, 40))
        textLabel2.setFont(QFont('Arial', 10))
        grifLayout.addWidget(textLabel1, 1, 1)
        grifLayout.addWidget(textLabel2, 2, 2)
        self.setLayout(grifLayout)
        self.resize(600, 500)
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
            if udienza.ID == str(tool.leggi):
                return udienza

    def getDatiC(self):
        self.loadDateC()
        tool = Tools()
        for cliente in self.clientiList:
            #if cliente.codiceFiscale == str(tool.leggi()): #Non legge, ricontrollare il metodo
            if cliente.codiceFiscale == 'cc':
                return cliente

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome = VistaHomeCliente()
        self.vistaHome.show()
        self.close()