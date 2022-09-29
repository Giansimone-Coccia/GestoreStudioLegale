from __future__ import print_function

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools

class VistaVisualizzaAppuntamento(QMainWindow):

    tool = Tools()
    appuntamentiList = tool.loadAppuntamenti()
    clientiList = tool.loadClienti()

    def __init__(self, parent = None):
        super(VistaVisualizzaAppuntamento, self).__init__(parent)

        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.grifLayout = QGridLayout()
        self.outerLayout.addWidget(self.tool.rewindButton(self.rewindHomeCliente), 1)
        labelC = QLabel()
        labelC.setText('Cliente: ' + '\n' + 'NOME: ' + f"{self.getDatiC()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.getDatiC()['Cognome']}" + '\n' + 'ID: ' + f"{self.getDatiC()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.getDatiC()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.getDatiC()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.getDatiC()['Numero telefono']}")
        self.outerLayout.addWidget(labelC, 0)
        labelC.setGeometry(QRect(0, 0, 350, 20))
        labelC.setFont(QFont('Arial', 10))
        labelC.setStyleSheet("border: 1px solid black;")
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiA()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Appuntamenti")
        self.show()

    def getDatiA(self):
        print("ciao6")
        tool = Tools()
        i = 1

        print("ciao7")
        for appuntamento in self.appuntamentiList:
            label = QLabel()
            print("ciao8")
            label.setText(
                'Appuntamento: ' + '\n' + 'Data e ora inizio: ' + f"{appuntamento.getDatiAppuntamento()['Data e Ora Inizio']}" + '\n' + 'Data e ora fine: ' + f"{appuntamento.getDatiAppuntamento()['Data e Ora Fine']}" + '\n' + 'ID: ' + f"{appuntamento.getDatiAppuntamento()['ID']}" + '\n' + 'Tipo procedimento: ' + f"{appuntamento.getDatiAppuntamento()['Tipo Procedimento']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            print("ciao9")
            label.setStyleSheet("border: 1px solid black;")
            print("ciao10")
            self.grifLayout.addWidget(label, i, 1, 1, 2)
            i += 1

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(self.tool.leggi(n=0)).rsplit()[0]:
                return cliente.getDatiCliente()

    def rewindHomeCliente(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
        self.vistaHome = VistaHomeAppuntamentiC()
        self.vistaHome.show()
        self.close()

    def getNum(self):
        n = 0
        self.appuntamentiList = self.tool.loadAppuntamenti()
        for appuntamento in self.appuntamentiList:
            n+=1
        return n