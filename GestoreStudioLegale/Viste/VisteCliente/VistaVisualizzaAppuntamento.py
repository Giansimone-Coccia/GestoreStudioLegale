from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaVisualizzaAppuntamento(QWidget):

    appuntamentiList = []
    clientiList = []

    def __init__(self, parent=None):
        super(VistaVisualizzaAppuntamento, self).__init__(parent)
        grifLayout = QGridLayout()
        tool = Tools()
        textLabel1 = QLabel()
        textLabel2 = QLabel()
        textLabel1.setText("Di seguito la lista delle parcelle con le relative informazioni")
        textLabel1.setGeometry(QRect(100, 120, 350, 40))
        textLabel1.setFont(QFont('Arial', 12))
        textLabel2.setText(f"{self.getDatiC()}")
        textLabel2.setGeometry(QRect(100, 120, 350, 40))
        textLabel2.setFont(QFont('Arial', 10))
        grifLayout.addWidget(tool.rewindButton(self.rewindHomeCliente), 0, 1)
        grifLayout.addWidget(textLabel1, 1, 1)
        grifLayout.addWidget(textLabel2, 2, 2)
        self.setLayout(grifLayout)
        self.resize(600, 500)
        self.setWindowTitle("Appuntamenti")
        self.show()

    def loadDateA(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamentiList = list(pickle.load(f))

    def loadDateC(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamentiList = list(pickle.load(f))

    def getDatiA(self):
        self.loadDateA()
        tool = Tools()
        for appuntamento in self.appuntamentiList:
            if appuntamento.ID == str(tool.leggi):
                return appuntamento

    def getDatiC(self):
        self.loadDateC()
        tool = Tools()
        for cliente in self.clientiList:
            #if cliente.codiceFiscale == str(tool.leggi()): #Non legge, ricontrollare il metodo
            if cliente.codiceFiscale == 'cc':
                return cliente

    def rewindHomeCliente(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
        self.vistaHome = VistaHomeAppuntamentiC()
        self.vistaHome.show()
        self.close()