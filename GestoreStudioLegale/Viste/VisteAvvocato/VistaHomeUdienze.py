from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente


#modificare dimensioni tasti in utilities
class VistaHomeUdienze(QMainWindow):

    udienzeList = []
    avvocatiList = []
    clientiList = []
    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeUdienze, self).__init__(parent)
        tool = Tools()


        '''self.scroll = QScrollArea()
        self.widget = QWidget()
        self.grifLayout = QGridLayout()
        self.grifLayout.addWidget(self.tool.rewindButton(self.rewind1), 0, 0)

        self.grifLayout.addWidget(tool.createButton("Inserisci", self.aggiungiUdienza), 0, 1)
        self.grifLayout.addWidget(
            tool.createButton("Cerca", self.cercaUdienza), 0, 2)'''

        self.cWidget = QWidget()  # contiene tutto
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind1), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(tool.createButton("Inserisci", self.aggiungiUdienza))
        self.button_layout.addWidget(tool.createButton("Cerca", self.cercaUdienza))
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiU()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        #self.setCentralWidget(self.scroll)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Parcelle")
        self.show()

    def getDatiU(self):
        self.udienzeList = self.tool.loadUdienze()
        self.avvocatiList = self.tool.loadAvvocati()
        tool = Tools()
        ud = []
        clientiL = []
        i=1

        print("ca")
        print(self.udienzeList)
        print(self.avvocatiList)
        #print(avvocato.getDatiAvvocato()['clienti'])

        for avvocato in self.avvocatiList:
            print("noia")
            print (self.tool.leggi().rsplit()[0])
            print (avvocato.codiceFiscale)
            print(avvocato.getDatiAvvocato()['clienti'])
            if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
               print("coglione")
               print(avvocato.getDatiAvvocato()['clienti'])
               clienti = avvocato.getDatiAvvocato()['clienti']
               print("ciao")
               print(clienti)
               print("cag")
               for cliente in clienti:
                   for udienza in self.udienzeList:
                      if udienza.Cliente.codiceFiscale == cliente.codiceFiscale:
                        print("cad")
                        ud.append(udienza)
                        print (ud)

        for u in ud:
            label = QLabel()
            print(u)
            textLabel2 = QLabel()
            textLabel2.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Numero telefono']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1,2)
            i += 1
            label.setText(
               'Udienza: ' + '\n' + 'CITTA TRIBUNALE: ' + f"{u.getDatiUdienza()['Città Tribunale']}" + '\n' + 'TIPO TRIBUNALE: ' + f"{u.getDatiUdienza()['Tipo Tribunale']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{u.getDatiUdienza()['Data e Ora Inizio']}" + '\n' + 'DATA ORA FINE: ' + f"{u.getDatiUdienza()['Data e Ora Fine']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            print("ciao2")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            self.grifLayout.addWidget(tool.createButton("Modifica", self.aggiornaUdienza), i, 1)
            self.grifLayout.addWidget(
                tool.createButton("Elimina", self.rimuoviUdienza),i,2)
            i += 1

            print("cos")

    def aggiungiUdienza(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaIserisciUdienza import VistaInserisciUdienza
        self.vistaInserimento = VistaInserisciUdienza()
        self.vistaInserimento.show()
        self.close()

    def aggiornaUdienza(self):
        pass

    def rimuoviUdienza(self):
        pass

    def cercaUdienza(self):
        pass

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        print(tool.leggi())
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                    return cliente.getDatiCliente()

    def rewind1(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaHome = VistaHomeAvvocato()
        self.vistaHome.show()
        self.close()
