from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout
import pickle
import os

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente


#modificare dimensioni tasti in utilities
class ParcellaRicercata(QMainWindow):

    parcelleList = []
    avvocatiList = []
    clientiList = []
    tool = Tools()

    def __init__(self, parcelle,parent=None):
        super(ParcellaRicercata, self).__init__(parent)
        tool = Tools()
        #print(parcelle[0].getDatiParcellaCliente()['intestatario']) #vuoto ma non crasha
        self.parcelleTrovate = []
        print("ciaoo45")
        for parcella in parcelle:
            self.parcelleTrovate.append(parcella)
            print("ciaoo89")
        print(self.parcelleTrovate)

        '''self.scroll = QScrollArea()
        self.widget = QWidget()
        self.grifLayout = QGridLayout()
        self.grifLayout.addWidget(self.tool.rewindButton(self.rewind1), 0, 0)

        self.grifLayout.addWidget(tool.createButton("Inserisci", self.aggiungiParcella), 0, 1)
        self.grifLayout.addWidget(
            tool.createButton("Cerca", self.cercaParcella), 0, 2)'''

        self.cWidget = QWidget()  # contiene tutto
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind1), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(tool.createButton("Inserisci", self.aggiungiParcella))
        self.button_layout.addWidget(tool.createButton("Cerca", self.cercaParcella))
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiP()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Parcelle")
        self.show()

    def getDatiP(self):
        self.parcelleList = self.tool.loadParcelle()
        self.avvocatiList = self.tool.loadAvvocati()
        tool = Tools()
        parc = []
        i=1

        #print("ca")
        #print(self.parcelleList)
        #print(self.avvocatiList)
        #print(avvocato.getDatiAvvocato()['clienti'])

        for avvocato in self.avvocatiList:
            #print("noia")
            print (self.tool.leggi().rsplit()[0])
            print (avvocato.codiceFiscale)
            print(avvocato.getDatiAvvocato()['clienti'])
            if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
               #print("coglione")
               print(avvocato.getDatiAvvocato()['clienti'])
               clienti = avvocato.getDatiAvvocato()['clienti']
               #print("ciao")
               print(clienti)
               #print("cag")
               for cliente in clienti:
                    #print("cioooo")
                    for parcella in self.parcelleList:
                        if parcella.Cliente.codiceFiscale == cliente.codiceFiscale:
                            #print("cad")
                            parc.append(parcella)
                            print (parc)

        for p in parc:
            label = QLabel()
            print(p)
            textLabel2 = QLabel()
            textLabel2.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{self.parcelleTrovate[p].getDatiParcellaCliente()['Cliente'].getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.parcelleTrovate[p].getDatiParcellaCliente()['Cliente'].getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{self.parcelleTrovate[p].getDatiParcellaCliente()['Cliente'].getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.parcelleTrovate[p].getDatiParcellaCliente()['Cliente'].getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.parcelleTrovate[p].getDatiParcellaCliente()['Cliente'].getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.parcelleTrovate[p].getDatiParcellaCliente()['Cliente'].getDatiCliente()['Numero telefono']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1, 2)
            i += 1
            label.setText(
                'Parcella: '+'\n'+ 'INTESTATARIO: '+f"{self.parcelleTrovate[p].getDatiParcellaCliente()['intestatario']}"+ '\n'+'IMPORTO: '+f"{self.parcelleTrovate[p].getDatiParcellaCliente()['importo']}"+'€'+'\n'+'ID: '+f"{self.parcelleTrovate[p].getDatiParcellaCliente()['ID']}"+'\n'+'IDENTIFICATIVO: '+f"{self.parcelleTrovate[p].getDatiParcellaCliente()['identificativo']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            print("ciao2")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            self.grifLayout.addWidget(tool.createButton("Modifica", self.aggiornaParcella), i, 1)
            self.grifLayout.addWidget(
                tool.createButton("Elimina", self.rimuoviParcella),i,2)
            i += 1

    def aggiungiParcella(self):
        pass

    def cercaParcella(self):
        pass

    def aggiornaParcella(self):
        pass

    def rimuoviParcella(self):
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